from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Kab_Sidrap

#Create your views here
class HomePageView(TemplateView):
    template_name = 'index.html'

def kabupaten_dataset(request):
    Kab_Sidrap = serialize('geojson', Kab_Sidrap.objects.all())
    return HttpResponse(Kab_Sidrap, content_type = 'json')