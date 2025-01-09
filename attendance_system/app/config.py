import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'dev-key-123'  # Development key
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Alovera@123@localhost/attendance_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'bishalgogoi09735@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Session settings
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = False
