from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<div><H1>Work in progress</H1></div><div><H3>CS Document Generator coming soon!</H3></div>"

if __name__ == '__main__':
    app.run(port=80,host='0.0.0.0')
