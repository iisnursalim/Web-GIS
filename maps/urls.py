from django.conf.urls import include, url
from .views import HomePageView, kabupaten_dataset

urlpatterns = [
    url('', HomePageView.as_view(), name = 'home'),
    url('data-kabupaten/', kabupaten_dataset, name = 'kabupaten')
]