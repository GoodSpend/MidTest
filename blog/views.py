from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from blog.models import BlogPost
from blog.forms import BlogPostForm
import datetime



# Create your views here.
#@login_required(login_url='login/')
def show_posts(request):
    post_data = BlogPost.objects.all()
    context = {
        'list_of_posts': post_data,
        'name': request.user.username,
        #'last_login': request.COOKIES['last_login'],

    }
    return render(request, "show_posts.html", context)

def create_post(request):
    form = BlogPostForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('blog:show_posts'))

    context = {'form': form}
    return render(request, "create_post.html", context)

def show_xml(request):
    data = BlogPost.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BlogPost.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request):
    data = BlogPost.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request):
    data = BlogPost.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def modify_post(request, id):
    # Get data berdasarkan ID
    blogpost = BlogPost.objects.get(pk = id)

    # Set instance pada form dengan data dari post
    form = BlogPostForm(request.POST or None, instance=blogpost)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('blog:show_posts'))

    context = {'form': form}
    return render(request, "modify_post.html", context)

def delete_post(request, id):
    # Get data berdasarkan ID
    blogpost = BlogPost.objects.get(pk = id)
    # Hapus data
    blogpost.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('blog:show_posts'))

@csrf_exempt
def create_post_ajax(request):  
# create object of form
    form = BlogPostForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = BlogPost.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'title':data.title,
            'content':data.content,
            'date':data.date,
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_post.html", context)

@csrf_exempt
def modify_post_ajax(request, id):  
# create object of form
    blogpost = BlogPost.objects.get(pk = id)

    # Set instance pada form dengan data dari post
    form = BlogPostForm(request.POST or None, instance=blogpost)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = BlogPost.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'title':data.title,
            'content':data.content,
            'date':data.date,
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "modify_post.html", context)