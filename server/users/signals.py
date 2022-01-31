from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Cart


# On user creation link a cart and send an email
def createAccount(sender, instance, created, **kwargs):
    if created:
        user = instance
        Cart.objects.create(user=user)
        subject = 'Welcome!'
        message = 'Thank you for signing up for my ecommerce demo project. This is a reminder that this is NOT a real store and you will not receive items you "purchase". Checkout will be handled with a test credit card.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False

        )

        # send_mail(
        #     'sub',
        #     'mess',
        #     'testemails105@gmail.com',
        #     'zanzong43@gmail.com',
        #     fail_silently=False

        # )


post_save.connect(createAccount, sender=User)

