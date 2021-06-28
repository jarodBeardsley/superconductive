from flask import Flask

app = Flask(__name__)

@app.route("/")
def time():
    return "1999-01-01T00:00:00.123456789"