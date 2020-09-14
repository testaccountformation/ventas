# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def index():
    return "ok"
    

@app.route('/login')
def login():
    return "login ok"


app.run(debug = True, port=5000)
