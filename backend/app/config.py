import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask Configuration
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_for_sessions')

    # Database Configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys and Other Secrets
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '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')
    FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY', 'AIzaSyA6kTCIbZZSHEL-0_EhLFQwsQfIQVDGA6g')

    # Firebase Configuration
    FIREBASE_CONFIG = {
        'apiKey': FIREBASE_API_KEY,
        'authDomain': "insightflowx.firebaseapp.com",
        'databaseURL': "https://insightflowx-default-rtdb.firebaseio.com",
        'projectId': "insightflowx",
        'storageBucket': "insightflowx.appspot.com",
        'messagingSenderId': "57199917829",
        'appId': "1:57199917829:web:8147748fcb5b8dbcf7956c",
        'measurementId': "G-SYGZ2PSS98"
    }

    # Pusher Configuration
    PUSHER_APP_ID = os.getenv('PUSHER_APP_ID', '1899482')
    PUSHER_KEY = os.getenv('PUSHER_KEY', '30647716200840e8a55d')
    PUSHER_SECRET = os.getenv('PUSHER_SECRET', '873220b603da75b08e5a')
    PUSHER_CLUSTER = os.getenv('PUSHER_CLUSTER', 'ap2')

    # Mailtrap Configuration
    MAILTRAP_API_TOKEN = os.getenv('MAILTRAP_API_TOKEN', 'f0aaffdb20014bc8e535540f89fad92a')
    MAILTRAP_USERNAME = os.getenv('MAILTRAP_USERNAME', '4608ba1265166f')
    MAILTRAP_PASSWORD = os.getenv('MAILTRAP_PASSWORD', 'd4fd0f0bf46404')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@insightflow.com')

config = Config()
