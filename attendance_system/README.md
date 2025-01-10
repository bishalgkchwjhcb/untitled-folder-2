# Face Recognition Attendance System

A Flask-based attendance system with face recognition capabilities.

## Features

- Face Recognition based attendance
- Student Registration
- Admin Dashboard
- Attendance Reports
- Email Notifications

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Deployment

This application is configured for deployment on Render. To deploy:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`
   - Python Version: 3.11.0

## Environment Variables

Required environment variables:
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: MySQL database URL
- `MAIL_USERNAME`: Email for notifications
- `MAIL_PASSWORD`: Email password
