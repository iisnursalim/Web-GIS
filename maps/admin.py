from django.contrib import admin
from .models import Jalan, Jembatan, Kesehatan, Drainase, Pendidikan, Kab_Sidrap
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class JalanAdmin(LeafletGeoAdmin):
	list_display = ('number','name')

class JembatanAdmin(LeafletGeoAdmin):
	list_display = ('nama','tipe_jem')

class KesehatanAdmin(LeafletGeoAdmin):
	list_display = ('namobj','alamat')

class DrainaseAdmin(LeafletGeoAdmin):
	list_display = ('lcode','panjang_m')

class PendidikanAdmin(LeafletGeoAdmin):
	list_display = ('namobj','alamat')

class Kab_SidrapAdmin(LeafletGeoAdmin):
	list_display = ('Desa','Kecamatan')

admin.site.register(Jalan, JalanAdmin)
admin.site.register(Jembatan, JembatanAdmin)
admin.site.register(Kesehatan, KesehatanAdmin)
admin.site.register(Drainase, DrainaseAdmin)
admin.site.register(Pendidikan, PendidikanAdmin)
admin.site.register(Kab_Sidrap, Kab_SidrapAdmin)