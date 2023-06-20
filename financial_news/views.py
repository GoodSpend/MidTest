from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from financial_news.models import News
from datetime import datetime
from django.core import serializers

@login_required(login_url='/login/')
def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

@login_required(login_url='/login/')
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financial_news:news_list')
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})

@login_required(login_url='/login/')
def news_update(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('financial_news:news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_update.html', {'form': form})

@login_required(login_url='/login/')
def news_delete(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('financial_news:news_list')
    return render(request, 'news_confirm_delete.html', {'news': news})

@csrf_exempt
def news_list(request):
    news = News.objects.all()
    return HttpResponse(serializers.serialize("json", news), content_type="application/json")

@csrf_exempt
def news_create_app(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        date_str = request.POST['date']
        date = datetime.strptime(date_str, "%d/%m/%Y").date()

        news = News(title=title, content=content, author=author, publish_date=date)
        news.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def news_update_app(request):
    news = News.objects.get(pk=int(request.POST['pk']))
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        date_str = request.POST['date']
        
        news.title = title
        news.content = content
        news.author = author
        news.publish_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        news.save()
        return HttpResponse(b"UPDATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def news_delete_app(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        news = News.objects.get(pk=int(pk))
        news.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()
