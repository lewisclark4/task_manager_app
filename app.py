import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")

@app.route('/')
def hello():
    return "Hello World"

app.run(host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", "5000")), debug=True)