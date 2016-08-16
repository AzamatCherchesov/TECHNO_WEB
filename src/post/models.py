# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from like.models import LikeMixin


class Post(LikeMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    blog = models.ManyToManyField('blog.Blog', verbose_name=u'Блог', related_name='posts')

    pub_date = models.DateField(auto_now_add=True, verbose_name=u'Дата публикации')
    changed = models.DateField(auto_now=True, verbose_name=u'Дата последнего опубликования')
    published = models.BooleanField(default=False, verbose_name=u'Опубликован')
    f = models.FileField()

    def get_cent_answers_channel_name(self):
        return "Comments"

    def __str__(self):
        return self.title
        # pub_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
