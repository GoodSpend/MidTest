from django.forms import ModelForm
from blog.models import BlogPost
from django import forms

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']