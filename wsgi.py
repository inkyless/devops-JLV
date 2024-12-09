from waitress import serve
from app import app
import os

if __name__ == "__main__":
    serve(app, listen="*:8080",
          url_scheme="https",threads=4)