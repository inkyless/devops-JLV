from waitress import serve
from app import app
import os

if __name__ == "__main__":
    serve(app, host='127.0.0.1', 
          port=int(os.environ.get('PORT', 8080)), 
          threads=8, 
          url_prefix='/api'
         )