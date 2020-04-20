from flask import Flask

def create_app():
  app = Flask(__name__)

  @app.route('/')
  def hello():
    return "welcome to cod loadouts bitches"
  
  return app