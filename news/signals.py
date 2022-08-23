from django.db.models.signals import post_save
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Post, SubscribersCategory
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(post_save, sender=SubscribersCategory)
def notify_user_subscribe(sender, instance, created, **kwargs):
    """Отправка письма при подписке на какую-либо категорию"""
    subject = f'Подписка оформлена!'
    send_mail(
        subject=subject,
        message=f'Вы успешно подписались на категорию {instance.category.name}',
        from_email='manageror@mail.ru',
        recipient_list=[f'{instance.subscriber.email}'],
    )


@receiver(post_save, sender=Post)
def notify_post_created(sender, instance, created, **kwargs):
    """Список адресов не собирается, прошу помощи в нахождении проблемы!"""
    recipient_list = []
    for category in instance.category.all():
        for subscriber in category.subscribers.all():
            email = f'{subscriber.email}'
            recipient_list.append(email)
    print(recipient_list)
    html_content = render_to_string('news/mail_subscribers.html', {'post': instance})
    msg = EmailMultiAlternatives(
        subject=f'{instance.title_post}',
        from_email='manageror@mail.ru',
        to=recipient_list
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
