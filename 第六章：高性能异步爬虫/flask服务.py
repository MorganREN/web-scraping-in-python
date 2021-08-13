# -*- coding:utf-8 -*-
"""
Author: Mohan Ren
Date: 08//13//2021//
"""
from flask import Flask
import asyncio
import time

app = Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return "Hello bobo"

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return "Hello jay"

@app.route('/mohan')
def index_mohan():
    time.sleep(2)
    return "Hello mohan"

# asyncio.sleep(2)

if __name__ == '__main__':
    app.run(threaded=True)
