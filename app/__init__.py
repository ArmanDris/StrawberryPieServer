from flask import Flask
from flask_cors import CORS
from .db import init_db, close_db
from .routes import bp

def create_app(test=False):
    app = Flask(__name__)
    if test:
        app.config['DATABASE'] = 'test'
    else:
        app.config['DATABASE'] = 'leaderboard'
    
    CORS(app)

    with app.app_context():
        init_db(app.config['DATABASE'])

    app.teardown_appcontext(close_db)
    
    app.register_blueprint(bp)
    
    return app