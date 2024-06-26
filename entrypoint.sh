#!/bin/bash

# use pip to install dependencies
#pip install -r requirements.txt

# Run the start script to initialize the database
python src/start.py

# Run the Flask application
export FLASK_APP=src/app.py
flask run --host=0.0.0.0 --port=5000