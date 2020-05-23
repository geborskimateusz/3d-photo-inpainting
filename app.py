import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from main import render_mp4
import boto3
import botocore
from tempfile import TemporaryDirectory
import os, os.path
from io import BytesIO
from PIL import Image
import uuid
from flask import send_file, send_from_directory, safe_join, abort

app = Flask(__name__)


@app.route("/render/<filer_name>", methods=["POST"])
def render(filer_name: str):
    if request.method == "POST":
        f = request.files["file"]

        with TemporaryDirectory() as tempdir:
            in_dir = TemporaryDirectory(dir=tempdir)
            out_dir = TemporaryDirectory(dir=tempdir)

            image = Image.open(BytesIO(f.read()))

            image.save(in_dir.name + "/image.jpg", "JPEG")

            render_mp4(in_dir.name, out_dir.name)

            filename = filer_name + ".mp4"
            return send_from_directory(out_dir.name, filename=filename, as_attachment=True)


if __name__ == "__main__":
    app.run()
