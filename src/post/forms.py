# coding=utf-8


from django import forms
from .models import Post


class PostListForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('answers_count', u'Колво ответов'),('id', 'ID'), ('pub_date', 'created')), required=False)


class QuesForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', "text", "blog", "f")
