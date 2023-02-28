#!/usr/bin/python3
"""Base Application for GiveTime"""
from flask import Flask


app = Flask('__name__')


@app.route('/')
def index():
    return "GiveTime"


if __name__ == "__main__":
    app.run(debug=True)