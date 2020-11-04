from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, include
from maps import views as maps_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),

	path('', include('maps.urls'),name='pagemaps'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('jalan/', user_views.JalanListView, name='list_jalan'),
    path('jalan/upload', user_views.uploadjalan, name='upload_jalan'),
    path('jalan/update/<int:pk>', user_views.JalanAttrUpdateView.as_view(), name='attr_jalan'),
    path('jalan/delete/<int:pk>', user_views.JalanDeleteView.as_view(),name='delete_jalan'),
    
    path('jembatan/', user_views.JembatanListView, name='list_jembatan'),
	path('jembatan/upload', user_views.uploadjembatan, name='upload_jembatan'),
    path('jembatan/update/<int:pk>', user_views.JembatanAttrUpdateView.as_view(), name='attr_jembatan'),
    path('jembatan/delete/<int:pk>', user_views.JembatanDeleteView.as_view(),name='delete_jembatan'),
    
    path('kesehatan/', user_views.KesehatanListView, name='list_kesehatan'),
    path('kesehatan/upload', user_views.uploadkesehatan, name='upload_kesehatan'),
    path('kesehatan/update/<int:pk>', user_views.KesehatanAttrUpdateView.as_view(), name='attr_kesehatan'),
    path('kesehatan/delete/<int:pk>', user_views.KesehatanDeleteView.as_view(),name='delete_kesehatan'),

    path('drainase/', user_views.DrainaseListView, name='list_drainase'),
    path('drainase/upload', user_views.uploaddrainase, name='upload_drainase'),
    path('drainase/update/<int:pk>', user_views.DrainaseAttrUpdateView.as_view(), name='attr_drainase'),
    path('drainase/delete/<int:pk>', user_views.DrainaseDeleteView.as_view(),name='delete_drainase'),

    path('pendidikan/', user_views.PendidikanListView, name='list_pendidikan'),
    path('pendidikan/upload', user_views.uploadpendidikan, name='upload_pendidikan'),
    path('pendidikan/update/<int:pk>', user_views.PendidikanAttrUpdateView.as_view(), name='attr_pendidikan'),
    path('pendidikan/delete/<int:pk>', user_views.PendidikanDeleteView.as_view(),name='delete_pendidikan'),

    path('kab_sidrap/', user_views.Kab_SidrapListView, name='list_kab_sidrap'),
    path('kab_sidrap/upload', user_views.uploadkab_sidrap, name='upload_kab_sidrap'),
    path('kab_sidrap/update/<int:pk>', user_views.Kab_SidrapAttrUpdateView.as_view(), name='attr_kab_sidrap'),
    path('kab_sidrap/delete/<int:pk>', user_views.Kab_SidrapDeleteView.as_view(),name='delete_kab_sidrap'),
]


