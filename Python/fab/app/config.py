import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = "app_124578_ap326598_app25879"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:brena123@localhost/appFAB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AUTH_TYPE = 1

    BABEL_DEFAULT_LOCALE = "pt_BR"
    BABEL_DEFAULT_FOLDER = "translations"
    LANGUAGES = {
        "pt_BR": {"flag": "br", "name": "Português (Brasil)"},
    }

    basedir = os.path.abspath(os.path.dirname(__file__))    
    
    UPLOAD_FOLDER = basedir + "/uploads"

    APP_THEME = "cosmo.css"
