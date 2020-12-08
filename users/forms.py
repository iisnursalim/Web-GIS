from django import forms
import floppyforms.__future__ as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

##------ USER -------##
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

##------ CUSTOM WIDGET ------##
class MultiPointWidget(forms.gis.MultiPointWidget, forms.gis.BaseOsmWidget):
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
    kelas_jln = forms.CharField(max_length=250)
    panjang = forms.FloatField()
    no_ruas = forms.CharField(max_length=250)
    nama_jalan = forms.CharField(max_length=250)
    tipe_perm = forms.CharField(max_length=250)
    kond_jalan = forms.CharField(max_length=250)
    lebar = forms.FloatField()
    geom = forms.gis.MultiLineStringField(widget=MultiLineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))


## ------ Jalan Point -------##
class JalanPointForm(forms.Form):
    surveyor = forms.CharField(max_length=254)
    waktu_surv = forms.DateField()
    nomor_ruas = forms.CharField(max_length=254)
    nama_jalan = forms.CharField(max_length=254)
    panjang = forms.CharField(max_length=254)
    lebar = forms.CharField(max_length=254)
    tpp = forms.CharField(max_length=254)
    tpu = forms.CharField(max_length=254)
    lhr = forms.CharField(max_length=254)
    klasifikas = forms.CharField(max_length=254)
    status_adm = forms.CharField(max_length=254)
    tipe_permu = forms.CharField(max_length=254)
    kondisi_ja = forms.CharField(max_length=254)
    hambatan = forms.CharField(max_length=254)
    tahun = forms.CharField(max_length=254)
    anggaran = forms.CharField(max_length=254)
    geom = forms.gis.MultiPointField(widget=MultiPointWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Jembatan -------##
class JembatanForm(forms.Form):
    surveyor = forms.CharField(max_length=254)
    waktu_surv = forms.DateField()
    nama = forms.CharField(max_length=254)
    no_kode = forms.CharField(max_length=254)
    pal_km = forms.CharField(max_length=254)
    tipe_sebra = forms.CharField(max_length=254)
    jenis_jemb = forms.CharField(max_length=254)
    panjang = forms.FloatField()
    lebar = forms.FloatField()
    jml_bentan = forms.FloatField()
    kondisi = forms.CharField(max_length=254)
    tahun = forms.CharField(max_length=254)
    anggaran = forms.FloatField()
    sumber_dan = forms.CharField(max_length=254)
    geom = forms.gis.MultiPointField(widget=MultiPointWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Fasilitas Kesehatan -------##
class KesehatanForm(forms.Form):
    surveyor = forms.CharField(max_length=254)
    waktu_surv = forms.DateField()
    nama = forms.CharField(max_length=254)
    alamat = forms.CharField(max_length=254)
    jenis = forms.CharField(max_length=254)
    jml_dokter = forms.CharField(max_length=254)
    jml_perawa = forms.CharField(max_length=254)
    jml_dosen = forms.CharField(max_length=254)
    jml_pasien = forms.CharField(max_length=254)
    fasilitas = forms.CharField(max_length=254)
    kondisi = forms.CharField(max_length=254)
    tahun_diba = forms.CharField(max_length=254)
    anggaran = forms.CharField(max_length=254)
    sumber_dan = forms.CharField(max_length=254)
    geom = forms.gis.MultiPointField(widget=MultiPointWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Drainase -------##
class DrainaseForm(forms.Form):
    surveyor = forms.CharField(max_length=254)
    waktu_surv = forms.DateField()
    no_kode = forms.CharField(max_length=254)
    rpru = forms.CharField(max_length=254)
    kemiringan = forms.CharField(max_length=254)
    pjg_salura = forms.FloatField()
    lebar_salu = forms.FloatField()
    kedalaman = forms.FloatField()
    kondisi = forms.CharField(max_length=254)
    tahun = forms.CharField(max_length=254)
    anggaran = forms.FloatField()
    sumber_dan = forms.CharField(max_length=254)
    geom = forms.gis.MultiLineStringField(widget=MultiLineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ Pendidikan -------##
class PendidikanForm(forms.Form):
    surveyor = forms.CharField(max_length=254)
    waktu_surv = forms.DateField()
    nama = forms.CharField(max_length=254)
    alamat = forms.CharField(max_length=254)
    jenjang = forms.CharField(max_length=254)
    jml_kelas = forms.FloatField()
    jml_guru = forms.FloatField()
    jml_siswa = forms.FloatField()
    fasilitas = forms.FloatField()
    tahun = forms.CharField(max_length=254)
    anggaran = forms.FloatField()
    geom = forms.gis.MultiPointField(widget=MultiPointWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ ADMINISTRASI KAB SIDRAP-------##
class Kab_SidrapForm(forms.Form):
    provinsi = forms.CharField(max_length=40)
    kecamatan = forms.CharField(max_length=40)
    desa = forms.CharField(max_length=40)
    kode2010 = forms.CharField(max_length=10)
    provno = forms.CharField(max_length=2)
    kabkotno = forms.CharField(max_length=2)
    kecno = forms.CharField(max_length=3)
    desano = forms.CharField(max_length=3)
    kabkot = forms.CharField(max_length=50)
    geom = forms.gis.MultiPolygonField(widget=MultiPolygonWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

    # TODO: Define form fields here


