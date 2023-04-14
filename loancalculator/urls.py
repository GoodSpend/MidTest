from django.urls import path
from . import views

app_name = 'loancalculator'

urlpatterns = [
    # path('ping', views.ping, name='ping'),
    path('form/', views.insert_loan_form, name='load_loanform'),
    path('ajax/', views.show_calculated_loan_ajax, name="getajax"),
    path('ajax-post/', views.post_calculated_loan_ajax, name="postajax"),
]