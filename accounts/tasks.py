from appointment_system.celery import app
from django.core.mail import send_mail
from django.conf import settings


@app.task
def email_to_customer(user_name, recipient):
    subject = 'Thank you for contacting us'
    message = f'Hello, {user_name}! We recieved your question ' \
        f'and we will answer as fast as we can. '
    print('minava email_to_customer')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient,]
    send_mail( subject, message, email_from, recipient_list )


@app.task
def email_to_admin(recipient, content):
    subject = f'You have new question from {recipient}'
    message = f'{content}'
    print('minava email_to_admin')
    email_from = recipient
    recipient_list = [settings.EMAIL_HOST_USER,]
    send_mail( subject, message, email_from, recipient_list )