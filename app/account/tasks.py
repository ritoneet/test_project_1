from celery import shared_task
from django.core.mail import send_mail

@shared_task
def my_fun():
    from time import sleep
    sleep(5)
    print("tasks completed")

@shared_task
def activate(activate_link, email_to):
    sub = "Поздравляем с регистрацией! Ссылка для активации ниже"

    body = (f"""Welcome to our site!

            Your activate link: {activate_link}

            Thanks, team.
            """)

    send_mail(
        sub,
        body,
        "djangotest2342465@gmail.com",
        [email_to],
        fail_silently=False,
    )
