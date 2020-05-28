FROM ubuntu:latest
LABEL  mateuszgeborski "mateuszgeborski@email.com"
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential
RUN pip3 install auxlib
FROM continuumio/miniconda3
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN conda create -n 3DPhotoCreator python=3.7 anaconda
# RUN conda activate 3DPhotoCreator
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit==10.1.243 -c pytorch
ENTRYPOINT ["python3"]
CMD ["app.py"]