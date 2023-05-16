from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
# login required
from django.contrib.auth.decorators import login_required

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
