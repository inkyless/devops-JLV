import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
from datetime import datetime as dt

upload_folder = "static/uploads"
extensions = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__, static_folder="static")

# App Config
app.config["SECRET_KEY"] = "SecretKey"
app.config["UPLOAD_FOLDER"] = upload_folder


# To verify file type
def allowed_file(filename):
    return "." in filename and filename.rsplit(".")[1].lower() in extensions


# Make APP route now
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def upload_file():
    # Check if post request has file part
    if request.method == "POST":
        if "file" not in request.files:
            flash("No File Part")
            return redirect(request.url)
    file = request.files["file"]

    # If user doesn't submit file, browser will submit empty file
    if file.filename == "":
        flash("No Selected File")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Save uploaded file as name of current time
        dt_now = dt.now().strftime("%Y%m%d%H%M%S$f")
        filename = dt.now + ".jpg"
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        # PATH to static files
        img_dir = "./static/uploads/"
        path = img_dir + filename
        # Import picture date
        img = cv2.imread(path)

        # If img has date
        if len(img) != 0:
            dt_now = dt.now().strftime("%Y%m%d%H%M%S$f")
            img_name = dt_now + ".jpg"
            # PATH to save directory
            img_path = img_dir + img_name
            cv2.imwrite(os.path.join(img_dir + img_name))
    return render_template("index.html", img_path=img_path)


if __name__ == "__main__":
    app.run()
