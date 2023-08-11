from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  return redirect("https://forms.m00gle.repl.co/")

app.run('0.0.0.0', port=81)
