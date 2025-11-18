from django import forms
from django.forms import widgets

from  webapp.models import  Tag

from  webapp.models import Article
from  django.core.exceptions import ValidationError

#from webapp.models import status_choices

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content',
                  'tags',
                  'author']
        #exclude = ('created_at', 'updated_at')
        widgets = {
            'title': widgets.Input(attrs={'class': 'form-control'}),
            'content': widgets.Textarea(attrs={'class': 'form-control'}),
            'author': widgets.Input(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError('заголовок не менее 3символов')
        return title

    def clean(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if title and content and title == content:
            raise ValidationError('заголовок и контент не должны совпадать')
        return super().clean()

