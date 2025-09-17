from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<div><H1>Work in progress</H1></div><div><H3>CS Document Generator coming soon!</H3></div>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

