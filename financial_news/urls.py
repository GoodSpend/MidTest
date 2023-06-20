from django.urls import path, include
from . import views

app_name = 'financial_news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('app', views.news_list, name='news_list'),
    path('news/new/', views.news_create, name='news_create'),
    path('news/new/app', views.news_create_app, name='news_create_app'),
    path('news/delete/app', views.news_delete_app, name='news_delete_app'),
    path('news/edit/app', views.news_update_app, name='news_update_app'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
    path('login/', include('home.urls')),
]
