from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Load environment variables from .env file
load_dotenv()

# Set Flask app secret key
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Set SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy database instance
db = SQLAlchemy(app)

# Import routes ( defined in app/routes/root.py)
from app.routes.root import *

