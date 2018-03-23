all: help

# prints a help message
help:
	@echo "'make install' to install dependencies."

# installs dependencies, and configures directory
install:
	echo "Checking for Python 3"
	@python3 --version
	mkdir -p input output images areas
	sudo apt-get install python3-pip
	pip3 install numpy scipy matplotlib
	@echo "Dependencies installed!"
