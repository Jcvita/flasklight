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
    utils.do_action(action="alert", color=rgb) 
    return redirect(url_for("/"))


@app.route("/rainbow/<freq>", methods=["POST"])
def rainbow(freq):
    utils.do_action(action="razer_rainbow", frequency=freq)
    return redirect(url_for("/"))

@app.route("/fill/<rgb>", methods=["POST"))
def fill(rgb):
    utils.do_action(action="fill", color=rgb)
    return redirect(url_for("/"))

@app.route("/party/<freq>", methods=["POST"])
def party(freq):
    utils.do_action(action="party", frequency=freq)
    return redirect(url_for("/"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

