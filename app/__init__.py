from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from .db import init_db, close_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)
    
    from .routes import *
    
    return app