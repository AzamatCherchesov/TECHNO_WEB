# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from like.models import LikeMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_email_notification
# Create your models here.

class Comment(LikeMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(verbose_name=u'Текст')
    post = models.ForeignKey('post.Post', verbose_name=u'Блог', related_name="comments")
    pub_date = models.DateField(auto_now_add=True, verbose_name=u'Дата публикации')
    changed = models.DateField(auto_now=True, verbose_name=u'Дата последнего опубликования')
    published = models.BooleanField(default=False, verbose_name=u'Опубликован')

    def as_compact_dict(self):
        result = {'id': self.id,
                  'text': self.text,
                  'pub_date': str(self.pub_date),
                  'post': self.post.pk,
                  'author': self.author.username}

        return result


    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'комментарии'


@receiver(post_save, sender=Comment, dispatch_uid="post_save_comment_centrifugo")
def comment_post_save(sender, instance=None, **kwargs):
    from adjacent import Client
    client = Client()
    client.publish(instance.post.get_cent_answers_channel_name(), instance.as_compact_dict())
    response = client.send()
    print(
        'sent to channel {}, got response from centrifugo: {}'.format(
            instance.post.get_cent_answers_channel_name(),
            response))


@receiver(post_save, sender=Comment, dispatch_uid="post_save_comment_email")
def on_comment_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        comment = instance
        send_email_notification.delay(
        'a1tt@rambler.ru',
        'New answer to question "{}"'.format(comment.post.title),
        'You got answer with the text: "{}"'.format(comment.text)
        )

# Create your models here.
