from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify

# Create your models here.

###  Jalan  ###
class Jalan(models.Model):
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
    tipe_ruas = models.CharField(max_length=100)
    geom = models.LineStringField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Jalan'

###  Jembatan  ###    
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
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Jembatan'

###  Fasilitas Kesehatan  ###
class Kesehatan(models.Model):
    namobj = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
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
        return self.namobj

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

###  Drainase  ###
class Drainase(models.Model):
    lcode = models.CharField(max_length=50)
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

###  Pendidikan  ###
class Pendidikan(models.Model):
    namobj = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)
    jml_kelas = models.IntegerField()
    jml_guru = models.IntegerField()
    jml_siswa = models.IntegerField()
    fasilitas = models.CharField(max_length=250)
    thn_bangun = models.IntegerField()
    anggaran = models.BigIntegerField()
    surveyor = models.CharField(max_length=100)
    surv_time = models.DateField()
    geom = models.PointField(srid=4326)
    
    def __unicode__(self):
        return self.namobj

    class Meta:
        verbose_name_plural = 'Pendidikan'

###  Administrasi Kabupaten Sidrap  ###
class Kab_Sidrap(models.Model):
    Provinsi = models.CharField(max_length=40)
    Kecamatan = models.CharField(max_length=40)
    Desa = models.CharField(max_length=40)
    Kabupaten = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.Provinsi

    class Meta:
        verbose_name_plural = 'Batas Administrasi'

