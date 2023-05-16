from django.forms import ModelForm
from .models import Data

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'type', 'amount', 'deadline', 'description']