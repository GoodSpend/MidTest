from django import forms
from django.db import models

class LoanForm(forms.Form):
    loan_amount = models.IntegerField(default=0)
    annual_interest = models.IntegerField(default=0)
    tenor = models.IntegerField(default=0)