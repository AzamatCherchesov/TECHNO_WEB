# -*- coding: utf-8 -*-
import datetime

from django.core.management import BaseCommand
from django.contrib.auth.models import User


import random

from post.models import Post

from blog.models import Blog




class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        s=[]
        for j in range(10):
              p = Blog()
              p.author = random.choice(users)
              p.title = u'title {}'.format(j)
              p.text = u'text {}'.format(j)
              p.pub_date = datetime.datetime.now()
              p.published = True
              p.save()
              s.append(p)
        for i in range(100):
            q = Post()

            q.author = random.choice(users)
            q.title = u'title {}'.format(i)
            q.text = u'text {}'.format(i)
            q.pub_date = datetime.datetime.now()
            q.published = True
            q.save()
            q.blog.add(random.choice(s))

