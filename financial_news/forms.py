from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    publish_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'publish_date']
