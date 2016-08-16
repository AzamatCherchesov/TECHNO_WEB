    # coding: utf-8
from __future__ import unicode_literals


from django.db import models
from django.conf import settings
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255,verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    pub_date = models.DateField(auto_now_add=True,verbose_name=u'Дата публикации')
    changed = models.DateField(auto_now=True,verbose_name=u'Дата последнего опубликования')
    published = models.BooleanField(default=False,verbose_name=u'Опубликован')
    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'

    def __unicode__(self):
        return self.title

