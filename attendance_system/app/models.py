from datetime import datetime
from flask_login import UserMixin
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    user_type = db.Column(db.Enum('student', 'admin'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    student = db.relationship('Student', backref='user', uselist=False)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    face_encoding = db.Column(db.LargeBinary)
    qr_code = db.Column(db.String(255))
    
    # Relationships
    attendances = db.relationship('Attendance', backref='student')

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    
    # Relationships
    attendances = db.relationship('Attendance', backref='subject')

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    entry_time = db.Column(db.DateTime, default=datetime.utcnow)
    verification_method = db.Column(db.Enum('qr', 'face', 'both'), nullable=False)
