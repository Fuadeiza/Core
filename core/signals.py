from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings


from .models import Order

from twilio.rest import Client


@receiver(post_save, sender=Order)
def confirmation_signal(sender, instance, created, **kwargs):
    if instance.confirmation_sent == False and instance.status == 'Completed':
        try:

            client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
            message = client.messages \
                .create(
                    body=f"تم تسليم طلبكم رقم {instance.order_id} نشكر لكم ثقتكم ببسكوتي ونتطلع لنيل شرف خدمتكم مرة أخرى.",
                    from_='+14637772322',
                    to=instance.phone
                )
            instance.confirmation_sent = True
            instance.save()
        except:
            print("Error While Sending Confirmation Message")