from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Potify',
        f'http://localhost:8000/account/activate/{code}/',
        'ajkanysdzumagulova@gmail.com',
        [email]
    )