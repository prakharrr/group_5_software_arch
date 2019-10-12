import subprocess
import sys
import time
import signal
import zmq
import traceback
import argparse

def main(exec_cmd, g_TO, g_N, g_heartbeat_addr, g_command_port):

    ctx = zmq.Context()
    end_time = 2
    # Connection to the heartbeats
    in_hb = ctx.socket(zmq.PULL)
    in_hb.bind(g_heartbeat_addr)

    # Connection to the outside world
    in_cmd = ctx.socket(zmq.PULL)
    in_cmd.bind(g_command_port)

    # setitng explicit retcode 1
    retcode = 1
    while retcode:
        print('[monitor] Running ' + exec_cmd + ' ... ')
 
        # signal.signal(signal.SIGINT, signal.SIG_IGN)

        all_is_well = True
        missed_TO = 0

        while True:
            try:
                (r, w, e) = zmq.select(
                        [in_hb, in_cmd], [], [], timeout=6)

                for sock in r:
                    msg = sock.recv() 

                    if sock == in_hb:
                        print ('[monitor] Got heartbeat.')

                        missed_TO = 0
                    elif sock == in_cmd:
                        print ('[monitor] Order to execute')
                        all_is_well = False
                        retcode = 'Killed by order'

                if end_time <= time.time():
                    end_time = time.time() + g_TO
                    print(end_time)
                    print ('[monitor] Missing a timeout ...')
                    missed_TO += 1

                if missed_TO >= g_N:
                    print ('[monitor] Killing off the process ...')
                    retcode = 'Missed ' + str(missed_TO) + ' heartbeats'
                    all_is_well = False

            except zmq.ZMQError as e:
                print ('[monitor] *** ZMQ had a problem: ' + str(e))
                traceback.print_exc()

            if not all_is_well:
                print ('[monitor] Probably already dead.')
                break 


        # Re-enable Ctrl-C handler to exit this wrapper
        signal.signal(signal.SIGINT, signal.default_int_handler)


    print ("[monitor] Exiting with return code 0")
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Wrapper for reliably executing programs within.')
    parser.add_argument(
            'exec_program',
            default ='random_app.py',
            help='the program to run in this wrapper')
    parser.add_argument(
            '--heartbeat-addr',
            '-b',
            default='ipc://heartbeat',
            help='address for receiving heartbeats')
    parser.add_argument(
            '--command-addr',
            '-c',
            default='ipc://command',
            help='address for receiving kill/restart command')
    parser.add_argument(
            '--heartbeat-timeout',
            '-t',
            type=float,
            default=1,
            help='period (in sec) of the heartbeats given by the program')
    parser.add_argument(
            '--misses-allowed',
            '-m',
            type=int,
            default=0,
            help='how many heartbeats missed before the program is killed')

    parsed_args = parser.parse_args()

    main(
            exec_cmd = parsed_args.exec_program,
            g_TO = parsed_args.heartbeat_timeout,
            g_N = parsed_args.misses_allowed,
            g_command_port = parsed_args.command_addr,
            g_heartbeat_addr = parsed_args.heartbeat_addr
            )

