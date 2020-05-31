FROM ubuntu:latest
FROM continuumio/miniconda:latest
LABEL  mateuszgeborski "mateuszgeborski@email.com"
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential
RUN pip3 install auxlib
COPY . /app
WORKDIR /app
RUN apt update
RUN apt install -y libfontconfig1-dev wget ffmpeg libsm6 libxext6 libxrender-dev mesa-utils-extra libegl1-mesa-dev libgles2-mesa-dev xvfb
RUN conda env create python=3.7 --file exported_conda_env.yml
SHELL ["conda", "run", "-n", "3DPhotoCreator", "/bin/bash", "-c"]
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["conda", "run", "-n", "3DPhotoCreator", "python", "app.py"]

