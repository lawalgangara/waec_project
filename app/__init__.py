from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object(Config)

# Set SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an instance of LoginManager and initialize it
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'

# Load environment variables from .env file
load_dotenv()

# Load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

db = SQLAlchemy(app)

from app.routes.root import *
from app.routes.admin import *
from app.models.user import *
from app.models.admin import *

