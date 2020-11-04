from django.urls import path
from . import views as maps_views

app_name='maps'

urlpatterns = [
	path('', maps_views.HomePageView.as_view(), name='home-maps'),	
	path('data-jalan/', maps_views.jalan_datasets, name = 'data_jalan'),
	path('data-jembatan/', maps_views.jembatan_datasets, name='data_jembatan'),
	path('data-kesehatan/', maps_views.kesehatan_datasets, name='data_kesehatan'),
    path('data-drainase/', maps_views.drainase_datasets, name='data_drainase'),
	path('data-pendidikan/', maps_views.pendidikan_datasets, name='data_pendidikan'),
    path('data-kab_sidrap/', maps_views.kab_sidrap_datasets, name='data_kab_sidrap'),
	
]