from itsdangerous import URLSafeTimedSerializer
from flask import current_app, url_for  # Add url_for import here
from flask_mail import Message
from app import mail
from app.models import User
from app.utils import send_email

def generate_reset_token(user):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(user.email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def verify_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=current_app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except:
        return None
    return User.query.filter_by(email=email).first()

def send_reset_email(user):
    token = generate_reset_token(user)
    reset_url = url_for('auth.reset_password', token=token, _external=True)
    subject = "Password Reset Request"
    sender = current_app.config['MAIL_DEFAULT_SENDER']
    recipients = [user.email]
    text_body = f"""To reset your password, visit the following link: {reset_url}"""
    html_body = f"""<p>To reset your password, visit the following link: <a href="{reset_url}">{reset_url}</a></p>"""
    send_email(subject, sender, recipients, text_body, html_body)
