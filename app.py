#! /usr/bin/python3.8
from flask import Flask, render_template, request, redirect, url_for
import requests, json
import utils

app = Flask(__name__)

@app.route("/")
def site():
    return render_template('index.html')


@app.route("/alert/<rgb>", methods=["POST"])
def alert(rgb):
    utils.alert(rgb) 
    return redirect(url_for("/"))


@app.route("/rainbow/<speed>", methods=["POST"])
def rainbow(speed):
    utils.razer_rainbow((float) speed)
    return redirect(url_for("/"))

@app.route("/fill/<rgb>", methods=["POST"))
def fill(rgb):
    utils.fill(rgb)
    return redirect(url_for("/"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

