from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe, like, and comment on this video, This is very interesting, Please try this as many as you want, TY!!!'
