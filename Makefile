#
# 
#

.PHONY: install warning run run_sender run_receiver
	
install: warning
	@echo "\nInstalling requirements!\n"
	pip3 install -r requirements.txt > /dev/null


warning:
	@echo "\n\n*****\nThis Makefile assumes you have Python3, Rabbit-MQ and PIKA installed!\
	\nIf not you can install it from here: \
	\nRabbitMQ -> https://www.rabbitmq.com/download.html\
	\nPika -> https://pika.readthedocs.io/en/stable/ \n***** \n\n"

run: warning run_receiver run_sender
	@echo "Running the application!!"

run_receiver:
	@echo "Running Receiver"
	python3 receiver.py

run_sender: 
	@echo "Running Sender"
	python3 sender.py