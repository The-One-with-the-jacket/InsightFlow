from flask import current_app, url_for
from flask_mail import Message
from app import mail
from app.utils import send_email

def send_group_invitation_email(user_email, group_name):
    subject = f"You've been invited to join {group_name}"
    sender = current_app.config['MAIL_DEFAULT_SENDER']
    recipients = [user_email]
    text_body = f"""You have been invited to join the group '{group_name}'. Click the link to accept the invitation."""
    html_body = f"""<p>You have been invited to join the group '<b>{group_name}</b>'. Click the link to accept the invitation.</p>"""
    send_email(subject, sender, recipients, text_body, html_body)
    