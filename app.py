from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Azure!HVE  hPPY learning!" 
