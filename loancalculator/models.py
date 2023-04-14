from django.db import models

class LoanCalculator(models.Model):
    loan_amount = models.IntegerField(default=0)
    annual_interest = models.IntegerField(default=0)
    tenor = models.IntegerField(default=0)
    monthly_payment = models.FloatField()
    accumulated_payment = models.FloatField()