from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Jalan, Jembatan, Kesehatan, Drainase, Pendidikan, Kab_Sidrap
from users import models as user_models

class HomePageView(TemplateView):
	template_name='home/index.html'

def jalan_datasets(request):
	jalan = serialize('geojson', Jalan.objects.all())
	return HttpResponse(jalan, content_type='json')

def jembatan_datasets(request):
	jembatan = serialize('geojson', Jembatan.objects.all())
	return HttpResponse(jembatan, content_type='json')

def kesehatan_datasets(request):
	kesehatan = serialize('geojson', Kesehatan.objects.all())
	return HttpResponse(kesehatan, content_type='json')

def drainase_datasets(request):
	drainase = serialize('geojson', Drainase.objects.all())
	return HttpResponse(drainase, content_type='json')

def pendidikan_datasets(request):
	pendidikan = serialize('geojson', Pendidikan.objects.all())
	return HttpResponse(pendidikan, content_type='json')

def kab_sidrap_datasets(request):
	kab_sidrap = serialize('geojson', Kab_Sidrap.objects.all())
	return HttpResponse(kab_sidrap, content_type='json')



