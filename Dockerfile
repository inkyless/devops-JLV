FROM python:3.10-bookworm
#Jangan python dari 3.12 ver ke atas karena perlu module distutils

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

#Referensi command prompt (waitress-serve --host=127.0.0.1 wsgi:app)
CMD [ "waitress-serve","--host=127.0.0.1","wsgi:app"]