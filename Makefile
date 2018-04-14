all:
	@echo "'make install' to install dependencies."

install:
	mkdir volumes output
	sudo apt-get install python-pip python3-pip mayavi2
	sudo -H pip3 install numpy scipy
	sudo -H pip install numpy
