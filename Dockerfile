FROM python:3.10-bookworm
#Jangan python dari 3.12 ver ke atas karena perlu module distutils

WORKDIR /app

RUN echo \
    && apt-get update \
    && apt-get --yes install apt-file \
    && apt-file update

RUN echo \
    && apt-get --yes install build-essential \ 
    && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

#Referensi command prompt (waitress-serve --host=127.0.0.1 wsgi:app)
CMD [ "waitress-serve","--listen=0.0.0.0:8080","wsgi:app"]