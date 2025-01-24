FROM tensorflow/tensorflow:latest

WORKDIR /app

# Set root user explicitly
USER root

COPY . /app

RUN echo \
    && apt-get update \
    && apt-get --yes install apt-file \
    && apt-get update && apt-get install -y net-tools \
    && apt-get --yes install build-essential \ 
    && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir pandas keras opencv-python   

EXPOSE 8080

CMD [ "waitress-serve","wsgi:app"]