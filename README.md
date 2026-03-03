Project's name : 
JSON API Cleaning & Logging

Objectives : 
This project fetches user data from a public API, processes and cleans nested JSON structures, removes unwanted keys, adds a generated age field, and stores the transformed data into a structured JSON file with a proper logging system.

The goal was to practice data manipulation, logging configuration, and project structuring in Python.

Technologies used : 
Python 3.11 
requests 
json 
jmespath 
logging 
JupyterLab

Features : 
Fetch data from a public API
Import and use a custom logging module
Clean nested JSON fields (e.g., remove geo from address)
Safely manipulate dictionaries without KeyErrors
Add a randomly generated age field
Save cleaned output into a JSON file
Configure logging with: console handler, file handler and prevention of duplicate handlers

What I learned : 
Mutable vs immutable objects, shallow vs deep copy, logging configuration and handlers (how to avoid duplicates).
Working directory and file paths, importing local modules in Jupyter, JSON manipulation.