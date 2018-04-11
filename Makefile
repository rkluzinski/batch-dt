all: help

# prints a help message
help:
	@echo "'make install' to install dependencies."

# installs dependencies, and configures directory
install:
	@echo "Checking for Python 3"
	@python3 --version
	sudo apt-get install python3-pip mayavi2
	pip3 install numpy scipy
	@echo "Dependencies installed!"

clean:
	@rm -rf *~
	@rm -rf __pycache__
