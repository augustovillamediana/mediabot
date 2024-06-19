#!/bin/bash

# Check if Python3 and venv are installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, please install Python3 to proceed."
    exit
fi

if ! python3 -m venv --help &> /dev/null
then
    echo "venv could not be found, please install venv to proceed."
    exit
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the application
python3 app.py "$@"