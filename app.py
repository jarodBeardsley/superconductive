"""Defines a REST endpoint with Flask that returns a UTC time

author: Jarod Beardsley
version: 06/28/2021
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def time():
    """Returns a UTC time in ISO format"""
    return "1968-10-01 00:00:00.123456789"
