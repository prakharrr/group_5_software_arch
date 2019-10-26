#
# Makefile targets
#


#
# Phony Targets
#

.PHONY: install run run_sender run_passivessa
	
install: run_sender run_passive
	@echo "\nInstalling requirements!\n"
	pip3 install -r requirements.txt > /dev/null


run: run_passive run_sender
	@echo "Running the application!!"


run_passive:
	@echo "Running Passive"
	@python3 passive.py

run_sender: 
	@echo "Running Sender"
	@python3 sender.py
