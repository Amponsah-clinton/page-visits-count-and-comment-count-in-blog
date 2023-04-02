from django.forms import ModelForm
from . models import Article,Comment
from django import forms


class BlogForm(ModelForm):
    class Meta:
      model = Article
      fields = "__all__"



class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'body',)


    