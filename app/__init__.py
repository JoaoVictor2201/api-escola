from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  db.init_app(app)
  Swagger(app)

  @app.route('/teste')
  def teste():
    return "<h1>API RODANDO</h1>"
  
  return app
