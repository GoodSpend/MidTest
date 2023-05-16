from django.urls import path, include
from . import views

app_name = 'financial_news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/new/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
    path('login/', include('home.urls')),
]
