import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from main import render_mp4
from tempfile import TemporaryDirectory
import os, os.path
from io import BytesIO
from PIL import Image
import uuid
from flask import send_file, send_from_directory, safe_join, abort, make_response, jsonify
import tempfile
import shutil
import logging
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/render/<filter_name>", methods=["POST"])
def render(filter_name):
    if request.method == "POST":
        f = request.files["file"]

        tempdir = tempfile.mkdtemp()
        in_dir = tempfile.mkdtemp(prefix="image_", dir=tempdir)
        out_dir = tempfile.mkdtemp(prefix="image_", dir=tempdir)

        image = Image.open(BytesIO(f.read()))
        image.save(in_dir + "/image.jpg", "JPEG")

        render_mp4(in_dir, out_dir, filter_name)

        filename = "image_" + filter_name + ".mp4"

        fout = open(os.path.join(out_dir, filename), "rb")
        response = make_response(fout.read())
        response.headers.set("Content-Type", "video/mp4")
        response.headers.set("Content-Disposition", "attachment", filename=filename)

        shutil.rmtree(tempdir)

        return  response


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e

    res = {'code': 500,
           'errorType': 'Internal Server Error',
           'errorMessage': "Something went really wrong!"}
    res['errorMessage'] = e.message if hasattr(e, 'message') else f'{e}'

    return jsonify(res), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
