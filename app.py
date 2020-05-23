import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from main import render

app = Flask(__name__)

@app.route("/get/<userid>", methods=["POST"])
def upload(userid: str):
    if request.method == "POST":
        image = request.files["file"]

        render(image)



if __name__ == "__main__":
    app.run()
