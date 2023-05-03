from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mark')
def markHTML():
    mark = ""
    mark = mark + Markup("<h2>Div 1</h2> \n<p>The contents of this div have been changed</p>")
    return mark


if __name__ == '__main__':
    app.run()
