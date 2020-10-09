from django.contrib import admin
from .models import Jalan, Jembatan, Kesehatan, Drainase, Kab_Sidrap
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class JalanAdm(LeafletGeoAdmin):
    list_display = ('Surveyor', 'Waktu_Survey')

admin.site.register(Jalan, JalanAdm)

class JembatanAdm(LeafletGeoAdmin):
    list_display = ('Surveyor', 'Tanggal_Survey')

admin.site.register(Jembatan, JembatanAdm)

class KesehatanAdm(LeafletGeoAdmin):
    list_display = ('Nama_Fasilitas_Kesehatan', 'Alamat')

admin.site.register(Kesehatan, KesehatanAdm)

class DrainaseAdm(LeafletGeoAdmin):
    list_display = ('Kode_Drainase', 'Tanggal_Survey')

admin.site.register(Drainase, DrainaseAdm)

class Kab_Sidrap_Adm(LeafletGeoAdmin):
    list_display = ('Desa', 'Kecamatan')

admin.site.register(Kab_Sidrap, Kab_Sidrap_Adm)

