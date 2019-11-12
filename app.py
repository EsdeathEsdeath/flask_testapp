from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
import psycopg2


from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')