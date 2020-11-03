from django import forms
import floppyforms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

##------ USER -------##
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

##------ CUSTOM WIDGET ------##
class PointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

class MultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

class MultiLineStringWidget(forms.gis.MultiLineStringWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

## ------ Jalan-------##
class JalanForm(forms.Form):
    surveyor = forms.CharField(max_length=250)
    surv_time = forms.DateField()
    number = forms.IntegerField()
    name = forms.CharField(max_length=250)
    length_km = forms.BigIntegerField()
    width_m = forms.BigIntegerField()
    tpp = forms.CharField(max_length=250)
    tpu = forms.CharField(max_length=250)
    lhr = forms.IntegerField()
    status = forms.CharField(max_length=100)
    surf_type = forms.CharField(max_length=100)
    kondisi = forms.CharField(max_length=100)
    hambatan = forms.CharField(max_length=100)
    tahun = forms.IntegerField()
    anggaran = forms.BigIntegerField()
    tipe_ruas = forms.CharField(max_length=100)
    geom = forms.gis.LineStringField (widget=LineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Jembatan -------##
class JembatanForm(forms.Form):
    surveyor = forms.CharField(max_length=100)
    surv_date = forms.DateField()
    nama = forms.CharField(max_length=100)
    pal_km = forms.IntegerField()
    panjang_m = forms.BigIntegerField()
    lebar_m = forms.BigIntegerField()
    bentang = forms.IntegerField()
    tipe_jem = forms.CharField(max_length=100)
    penyebrang = forms.CharField(max_length=100)
    bhn_konstr = forms.CharField(max_length=50)
    kondisi = forms.CharField(max_length=100)
    tahun = forms.IntegerField()
    anggaran = forms.BigIntegerField()
    geom = forms.gis.PointField(widget=PointWidget(attrs={
        'id': 'gis',
        'style': 'widformsth: 100%;'
    }))

##------ Fasilitas Kesehatan -------##
class KesehatanForm(forms.Form):
    namobj = forms.CharField(max_length=250)
    alamat = forms.CharField(max_length=250)
    remark = forms.CharField(max_length=250)
    jml_dktr = forms.IntegerField()
    jml_prwt = forms.IntegerField()
    jml_pasien = forms.IntegerField()
    jml_ruang = forms.IntegerField()
    fasilitas = forms.CharField(max_length=250)
    kond_bgnn = forms.CharField(max_length=100)
    tahun = forms.IntegerField()
    anggaran = forms.BigIntegerField()
    sumb_dana = forms.CharField(max_length=50)
    kontraktor = forms.CharField(max_length=100)
    surv_time = forms.DateField()
    geom = forms.gis.PointField(widget=PointWidget(attrs={
        'id': 'gis',
        'style': 'widformsth: 100%;'
    }))

##------ Drainase -------##
class DrainaseForm(forms.Form):
    lcode = forms.CharField(max_length=50)
    rpru = forms.CharField(max_length=100)
    kemiringan = forms.IntegerField()
    panjang_m = forms.IntegerField()
    kdlmn_m = forms.IntegerField()
    kondisi = forms.CharField(max_length=50)
    tahun = forms.IntegerField()
    anggaran = forms.BigIntegerField()
    kontraktor = forms.CharField(max_length=50)
    surv_time = forms.DateField()
    geom = forms.gis.LineStringField (widget=LineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Pendidikan -------##
class PendidikanForm(forms.Form):
    namobj = forms.CharField(max_length=250)
    remark = forms.CharField(max_length=250)
    alamat = forms.CharField(max_length=250)
    jml_kelas = forms.IntegerField()
    jml_guru = forms.IntegerField()
    jml_siswa = forms.IntegerField()
    fasilitas = forms.CharField(max_length=250)
    thn_bangun = forms.IntegerField()
    anggaran = forms.BigIntegerField()
    surveyor = forms.CharField(max_length=100)
    surv_time = forms.DateField()
    geom = forms.gis.PointField(widget=PointWidget(attrs={
        'id': 'gis',
        'style': 'widformsth: 100%;'
    }))

##------ ADMINISTRASI KAB SIDRAP-------##
class Kab_SidrapForm(forms.Form):
    Provinsi = forms.CharField(max_length=40)
    Kecamatan = forms.CharField(max_length=40)
    Desa = forms.CharField(max_length=40)
    Kabupaten = forms.CharField(max_length=50)
    geom = forms.gis.MultiPolygonField(widget=MultiPolygonWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

    # TODO: Define form fields here


