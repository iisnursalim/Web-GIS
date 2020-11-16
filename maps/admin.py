from django.contrib import admin
from .models import Jalan, JalanPoint, Jembatan, Kesehatan, Drainase, Pendidikan, Kab_Sidrap
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class Jalan_Admin(LeafletGeoAdmin):
	list_display = ('nama_jalan','panjang', 'kelas_jln')

class JalanPoint_Admin(LeafletGeoAdmin):
	list_display = ('nomor_ruas','nama_jalan', 'status_adm')

class Jembatan_Admin(LeafletGeoAdmin):
	list_display = ('no_kode','nama', 'tipe_sebra')

class Kesehatan_Admin(LeafletGeoAdmin):
	list_display = ('nama','alamat', 'jenis')

class Drainase_Admin(LeafletGeoAdmin):
	list_display = ('no_kode','rpru', 'kondisi')

class Pendidikan_Admin(LeafletGeoAdmin):
	list_display = ('nama','alamat', 'jenjang')

class Kab_Sidrap_Admin(LeafletGeoAdmin):
	list_display = ('desa','kecamatan')

admin.site.register(Jalan, Jalan_Admin)
admin.site.register(JalanPoint, JalanPoint_Admin)
admin.site.register(Jembatan, Jembatan_Admin)
admin.site.register(Kesehatan, Kesehatan_Admin)
admin.site.register(Drainase, Drainase_Admin)
admin.site.register(Pendidikan, Pendidikan_Admin)
admin.site.register(Kab_Sidrap, Kab_Sidrap_Admin)