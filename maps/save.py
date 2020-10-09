from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Jalan(models.Model):
    remark = models.CharField(max_length=250)
    shape_leng = models.FloatField()
    surveyor = models.CharField(max_length=250)
    surv_time = models.DateField()
    number = models.IntegerField()
    name = models.CharField(max_length=250)
    length_km = models.BigIntegerField()
    width_m = models.BigIntegerField()
    tpp = models.CharField(max_length=250)
    tpu = models.CharField(max_length=250)
    lhr = models.IntegerField()
    status = models.CharField(max_length=100)
    surf_type = models.CharField(max_length=100)
    kondisi = models.CharField(max_length=100)
    hambatan = models.CharField(max_length=100)
    tahun = models.IntegerField()
    anggaran = models.BigIntegerField()
    geom = models.LineStringField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Jalan'
    
class Jembatan(models.Model):
    surveyor = models.CharField(max_length=100)
    surv_date = models.DateField()
    nama = models.CharField(max_length=100)
    pal_km = models.IntegerField()
    panjang_m = models.BigIntegerField()
    lebar_m = models.BigIntegerField()
    bentang = models.IntegerField()
    tipe_jem = models.CharField(max_length=100)
    penyebrang = models.CharField(max_length=100)
    bhn_konstr = models.CharField(max_length=50)
    kondisi = models.CharField(max_length=100)
    tahun = models.IntegerField()
    anggaran = models.BigIntegerField()
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Jembatan'

class Kesehatan(models.Model):
    namobj = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)
    jml_dktr = models.IntegerField()
    jml_prwt = models.IntegerField()
    jml_pasien = models.IntegerField()
    jml_ruang = models.IntegerField()
    fasilitas = models.CharField(max_length=250)
    kond_bgnn = models.CharField(max_length=100)
    tahun = models.IntegerField()
    anggaran = models.BigIntegerField()
    sumb_dana = models.CharField(max_length=50)
    kontraktor = models.CharField(max_length=100)
    surv_time = models.DateField()
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.namaobj

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

class Drainase(models.Model):
    lcode = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    rpru = models.CharField(max_length=100)
    kemiringan = models.IntegerField()
    panjang_m = models.IntegerField()
    kdlmn_m = models.IntegerField()
    kondisi = models.CharField(max_length=50)
    tahun = models.IntegerField()
    anggaran = models.BigIntegerField()
    kontraktor = models.CharField(max_length=50)
    surv_time = models.DateField()
    geom = models.LineStringField(srid=4326)
    
    def __unicode__(self):
        return self.lcode

    class Meta:
        verbose_name_plural = 'Drainase'

class Kab_Sidrap(models.Model):
    provinsi = models.CharField(max_length=40)
    kecamatan = models.CharField(max_length=40)
    desa = models.CharField(max_length=40)
    sumber = models.CharField(max_length=50)
    kode2010 = models.CharField(max_length=10)
    provno = models.CharField(max_length=2)
    kabkotno = models.CharField(max_length=2)
    kecno = models.CharField(max_length=3)
    desano = models.CharField(max_length=3)
    kabkot = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.kecamatan

    class Meta:
        verbose_name_plural = 'Batas Administrasi'



#load.py file
import os
from django.contrib.gis.utils import LayerMapping
from .models import Jalan, Jembatan, Kesehatan, Drainase, Kab_Sidrap
    
jalan_mapping = {
    'remark': 'REMARK',
    'shape_leng': 'SHAPE_Leng',
    'surveyor': 'SURVEYOR',
    'surv_time': 'SURV_TIME',
    'number': 'NUMBER',
    'name': 'NAME',
    'length_km': 'LENGTH_KM',
    'width_m': 'WIDTH_M',
    'tpp': 'TPP',
    'tpu': 'TPU',
    'lhr': 'LHR',
    'status': 'STATUS',
    'surf_type': 'SURF_TYPE',
    'kondisi': 'KONDISI',
    'hambatan': 'HAMBATAN',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'geom': 'LINESTRING25D',
}

jalan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jalan.shp'),
)

jembatan_mapping = {
    'surveyor': 'SURVEYOR',
    'surv_date': 'SURV_DATE',
    'nama': 'NAMA',
    'pal_km': 'PAL_KM',
    'panjang_m': 'PANJANG_M',
    'lebar_m': 'LEBAR_M',
    'bentang': 'BENTANG',
    'tipe_jem': 'TIPE_JEM',
    'penyebrang': 'PENYEBRANG',
    'bhn_konstr': 'BHN_KONSTR',
    'kondisi': 'KONDISI',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'geom': 'POINT25D',
}

jembatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jembatan.shp'),
)

kesehatan_mapping = {
    'namobj': 'NAMOBJ',
    'remark': 'REMARK',
    'alamat': 'ALAMAT',
    'jml_dktr': 'JML_DKTR',
    'jml_prwt': 'JML_PRWT',
    'jml_pasien': 'JML_PASIEN',
    'jml_ruang': 'JML_RUANG',
    'fasilitas': 'FASILITAS',
    'kond_bgnn': 'KOND_BGNN',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'sumb_dana': 'SUMB_DANA',
    'kontraktor': 'KONTRAKTOR',
    'surv_time': 'SURV_TIME',
    'geom': 'POINT25D',
}

kesehatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kesehatan.shp'),
)

drainase_mapping = {
    'lcode': 'LCODE',
    'shape_leng': 'SHAPE_Leng',
    'rpru': 'RPRU',
    'kemiringan': 'KEMIRINGAN',
    'panjang_m': 'PANJANG_M',
    'kdlmn_m': 'KDLMN_M',
    'kondisi': 'KONDISI',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'kontraktor': 'KONTRAKTOR',
    'surv_time': 'SURV_TIME',
    'geom': 'LINESTRING25D',
}

drainase_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Drainase.shp'),
)

kab_sidrap_mapping = {
    'provinsi': 'PROVINSI',
    'kecamatan': 'KECAMATAN',
    'desa': 'DESA',
    'sumber': 'SUMBER',
    'kode2010': 'KODE2010',
    'provno': 'PROVNO',
    'kabkotno': 'KABKOTNO',
    'kecno': 'KECNO',
    'desano': 'DESANO',
    'kabkot': 'KABKOT',
    'geom': 'MULTIPOLYGON',
}

kab_sidrap_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kab_Sidrap.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Jalan, jalan_shp, jalan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):    
    lm = LayerMapping(Jembatan, jembatan_shp, jembatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kesehatan, kesehatan_shp, kesehatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):
    lm = LayerMapping(Drainase, drainase_shp, drainase_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kab_Sidrap, kab_sidrap_shp, kab_sidrap_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


