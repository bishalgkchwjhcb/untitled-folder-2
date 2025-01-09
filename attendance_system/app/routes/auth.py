from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from .. import db
from ..models import User, Student

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('register.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        student_id = request.form.get('student_id')
        department = request.form.get('department')

        # Validate input
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'error': 'Email already exists'}), 400

        try:
            # Create user and student
            user = User(
                email=email,
                password_hash=generate_password_hash(password),
                user_type='student'
            )
            db.session.add(user)
            db.session.flush()

            student = Student(
                user_id=user.id,
                student_id=student_id,
                full_name=full_name,
                department=department,
                semester=6
            )
            db.session.add(student)
            db.session.commit()

            return jsonify({'message': 'Registration successful'}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if user.user_type == 'admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('student.dashboard'))

        flash('Invalid email or password')
        return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
