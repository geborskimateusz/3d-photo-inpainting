import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from main import render
import boto3
import botocore
from tempfile import TemporaryDirectory
import os, os.path
from io import BytesIO
from PIL import Image

BUCKET_NAME = "insta3d"

app = Flask(__name__)


@app.route("/get/<user_id>/<image_id>", methods=["GET"])
def upload(userid: str, image_id: str):
    if request.method == "GET":
        bucket_file_name = userid + "/" + image_id + "/image/penguinuhh-c8HSJgY2Do4-unsplash.jpg"

        input_dir = download_s3_file(bucket_file_name)

        render(input_dir)


if __name__ == "__main__":
    app.run()


def download_s3_file(bucket_file_name: str):
    s3 = boto3.client("s3")
    with TemporaryDirectory() as tempdir:
        # tempdir = tempfile.mkdtemp(prefix="myapplication-", suffix="image")
        file_byte_string = s3.get_object(Bucket=BUCKET_NAME, Key=bucket_file_name)["Body"].read()
        image = Image.open(BytesIO(file_byte_string))

        image.save(tempdir + "/image.jpg", "JPEG")

        return tempdir
