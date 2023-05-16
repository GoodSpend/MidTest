from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Data
from .forms import DataForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def show_data(request):
    data = Data.objects.all()
    context = {
        'list_of_datas': data,
        'name': request.user.username,
    }
    return render(request, "data.html", context)

def create_data(request):
    form = DataForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('data:show_data'))

    context = {'form': form}
    return render(request, "create_data.html", context)

def show_xml(request):
    xml_data = Data.objects.all()
    return HttpResponse(serializers.serialize("xml", xml_data), content_type="application/xml")

def show_json(request):
    json_data = Data.objects.all()
    return HttpResponse(serializers.serialize("json", json_data), content_type="application/json")

def show_xml_by_id(request, id):
    xml_id_data = Data.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", xml_id_data), content_type="application/xml")

def show_json_by_id(request, id):
    json_id_data = Data.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", json_id_data), content_type="application/json")

def modify_data(request, id):
    # Get data berdasarkan ID
    data = Data.objects.get(pk = id)

    # Set instance pada form dengan data yang baru saja didapat
    form = DataForm(request.POST or None, instance=data)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('data:show_data'))

    context = {'form': form}
    return render(request, "modify_data.html", context)

def delete_data(request, id):
    # Get data berdasarkan ID
    data = Data.objects.get(pk = id)
    # Hapus data
    data.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('data:show_data'))

@csrf_exempt
def create_data_ajax(request):  
    # create object of form
    form = DataForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = Data.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'name':data.name,
            'date':data.date,
            'type':data.type,
            'amount':data.amount,
            'deadline':data.deadline,
            'description':data.description,
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_data.html", context)
