import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
from datetime import datetime as dt
import keras
import numpy as np

# Initialize Flask and set upload folder
app = Flask(__name__)
upload_folder = "static/uploads"
app.config["SECRET_KEY"] = "SecretKey"
app.config["UPLOAD_FOLDER"] = upload_folder

# Allowed file extensions
extensions = {"png", "jpg", "jpeg"}

# Load the pre-trained model
model_path = "static/models/manggo.h5"  # Path to your model
model = keras.saving.load_model(model_path)

# Class labels
labels = ["mangga_busuk", "mangga_matang", "kurang_matang"]


# To verify file type
def allowed_file(filename):
    return "." in filename and filename.rsplit(".")[1].lower() in extensions


def prepare_image(image_path):
    """Prepare the image for prediction by resizing and scaling"""
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150, 150))  # Ubah ukuran gambar menjadi 150x150
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0  # Normalisasi ke rentang [0,1]
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch
    return img


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Make APP route now
@app.route("/result", methods=["POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dt_now = dt.now().strftime("%Y%m%d%H%M%S%f")
            filename = dt_now + ".jpg"
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Prepare and predict
            img = prepare_image(file_path)
            predictions = model.predict(img)
            class_index = np.argmax(predictions[0])  # Get index of highest probability
            ripeness_status = labels[class_index]  # Map index to label
            confidence = predictions[0][class_index] * 100  # Get confidence percentage

            return render_template(
                "index.html",
                img_path=file_path,
                result=ripeness_status,
                confidence=confidence,
            )
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
