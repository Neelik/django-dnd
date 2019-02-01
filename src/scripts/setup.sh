#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu" ]]; then
        echo "Detected $OSTYPE."
	echo "Beginning installation of dev packages..."
	sudo apt-get install libffi-dev python3.5-dev
	echo "Activating virtual environment..."
	source ../../../bin/activate
	echo "Installing requirements.txt dependencies..."
	pip install -r ../requirements.txt
    if [ "$1" == "-d" ]; then
        echo "Performing Database creation"; ./database.sh
    fi
	echo "INSTALLATION COMPLETE! Reminder: Activate your virtual environment to begin development ;)"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Detected MacOS"
elif [[ "$OSTYPE" == "cygwin" ]]; then
	echo "Detected Linux on Windows"
else
	echo "OSTYPE $OSTYPE not supported by this package."
fi