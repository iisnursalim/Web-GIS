from django.contrib import admin
from .models import Jalan, Jembatan, Kesehatan, Drainase, Pendidikan, Kab_Sidrap
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class Jalan_Admin(LeafletGeoAdmin):
	list_display = ('number','name')

class Jembatan_Admin(LeafletGeoAdmin):
	list_display = ('nama','tipe_jem')

class Kesehatan_Admin(LeafletGeoAdmin):
	list_display = ('namobj','remark')

class Drainase_Admin(LeafletGeoAdmin):
	list_display = ('lcode','rpru')

class Pendidikan_Admin(LeafletGeoAdmin):
	list_display = ('namobj','remark')

class Kab_Sidrap_Admin(LeafletGeoAdmin):
	list_display = ('desa','kecamatan')

admin.site.register(Jalan, Jalan_Admin)
admin.site.register(Jembatan, Jembatan_Admin)
admin.site.register(Kesehatan, Kesehatan_Admin)
admin.site.register(Drainase, Drainase_Admin)
admin.site.register(Pendidikan, Pendidikan_Admin)
admin.site.register(Kab_Sidrap, Kab_Sidrap_Admin)