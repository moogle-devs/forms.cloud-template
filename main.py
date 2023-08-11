from flask import Flask, request, redirect, jsonify
from os import mkdir, chdir, listdir

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  return redirect("https://forms.m00gle.repl.co/")

@app.route('/', methods=["POST"])
def req():
  data = request.get_json(force=True)
  user = data["user"]
  if user not in listdir():
    mkdir(user)
  chdir(user)
  with open(data["id"] + ".json", "w") as file:
    file.write(data["content"])
  return jsonify({ "success": True, "path": f"{user}/{id}.json" })

app.run('0.0.0.0', port=81)
