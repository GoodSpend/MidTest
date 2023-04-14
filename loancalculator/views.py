import json
from .models import LoanCalculator
from .forms import LoanForm
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# @login_required(login_url='/login/')
def show_calculated_loan(request):
    return render(request, "loan_form.html")

# @login_required(login_url='/login/')
def insert_loan_form(request):
    form = LoanForm()
    context = {
        'form':form
        }
    
    return render(request, 'loan_form.html', context)

def calculate_monthly_payment(loan_amount, annual_interest, tenor):
    total_month = tenor * 12
    interest_per_month = ((annual_interest / 100) / total_month) * loan_amount
    monthly_payment = loan_amount / tenor + interest_per_month
    
    return monthly_payment

def calculate_total_payment(loan_amount, annual_interest, tenor):
    total_payment = loan_amount + (loan_amount * (annual_interest / 100))

    return total_payment

# @login_required(login_url='/login/')
def show_calculated_loan_ajax(request):
    loan_data = LoanCalculator.objects.all()
    response = serializers.serialize("json", loan_data)
    
    return HttpResponse(response, content_type="application/json")

# @login_required(login_url='/login/')
@csrf_exempt
def post_calculated_loan_ajax(request):
    if request.method == 'POST':
        loan_amount = float(request.POST["loan_amount"])
        annual_interest = float(request.POST["annual_interest"])
        tenor = float(request.POST["tenor"])
        
        instance = LoanCalculator(loan_amount = loan_amount, annual_interest = annual_interest, tenor = tenor, monthly_payment = calculate_monthly_payment(loan_amount, annual_interest, tenor), accumulated_payment = calculate_total_payment(loan_amount, annual_interest, tenor))
        instance.save()
        
        data = {
            "message": 'Loan calculated successfully!',
            "data": model_to_dict(instance)
        }
        json_object = json.dumps(data, indent = 4) 

        return JsonResponse(json.loads(json_object))
    
    return redirect("loancalculator:insert_loan_form")

# def ping(request):
#     return render(request, "home.html")