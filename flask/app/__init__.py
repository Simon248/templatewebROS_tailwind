from flask import Flask

# from config import Config

app = Flask(__name__,static_url_path='')

from app import routes
