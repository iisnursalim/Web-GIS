from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify

# Create your models here.

###  Jalan  ###
class Jalan(models.Model):
    surveyor = models.CharField(max_length=250, default=' ')
    surv_time = models.DateField(default=' ')
    number = models.IntegerField(default=' ')
    name = models.CharField(max_length=250, default=' ')  
    tpp = models.CharField(max_length=250, default=' ')   
    tpu = models.CharField(max_length=250, default=' ')   
    lhr = models.IntegerField(default=' ')
    status = models.CharField(max_length=100, default=' ')
    surf_type = models.CharField(max_length=100, default=' ')
    kondisi = models.CharField(max_length=100, default=' ')
    hambatan = models.CharField(max_length=100, default=' ')
    tahun = models.IntegerField(default=' ')
    length_km = models.IntegerField(default=' ')
    width_m = models.IntegerField(default=' ')
    anggaran = models.IntegerField(default=' ')
    klas_ruas = models.CharField(max_length=250, default=' ')
    geom = models.MultiLineStringField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Jalan'

###  Jembatan  ###    
class Jembatan(models.Model):
    surveyor = models.CharField(max_length=100, default=' ')
    surv_date = models.DateField(default=' ')
    nama = models.CharField(max_length=100, default=' ')
    pal_km = models.IntegerField(default=' ')
    bentang = models.IntegerField(default=' ')
    tipe_jem = models.CharField(max_length=100, default=' ')
    penyebrang = models.CharField(max_length=100, default=' ')
    bhn_konstr = models.CharField(max_length=50, default=' ')
    kondisi = models.CharField(max_length=100, default=' ')
    tahun = models.IntegerField(default=' ')
    panjang_m = models.IntegerField(default=' ')
    lebar_m = models.IntegerField(default=' ')
    anggaran = models.IntegerField(default=' ')
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Jembatan'

###  Fasilitas Kesehatan  ###
class Kesehatan(models.Model):
    namobj = models.CharField(max_length=250, default=' ')
    remark = models.CharField(max_length=250, default=' ')
    alamat = models.CharField(max_length=250, default=' ')
    jml_dktr = models.IntegerField(default=' ')
    jml_prwt = models.IntegerField(default=' ')
    jml_pasien = models.IntegerField(default=' ')
    jml_ruang = models.IntegerField(default=' ')
    fasilitas = models.CharField(max_length=250, default=' ')
    kond_bgnn = models.CharField(max_length=100, default=' ')
    tahun = models.IntegerField(default=' ')
    sumb_dana = models.CharField(max_length=50, default=' ')
    kontraktor = models.CharField(max_length=100, default=' ')
    surv_time = models.DateField(default=' ')
    anggaran = models.IntegerField(default=' ')
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.namobj

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

###  Drainase  ###
class Drainase(models.Model):
    lcode = models.CharField(max_length=50, default=' ')
    rpru = models.CharField(max_length=100, default=' ')
    kemiringan = models.IntegerField(default=' ')
    panjang_m = models.IntegerField(default=' ')
    kdlmn_m = models.IntegerField(default=' ')
    kondisi = models.CharField(max_length=50, default=' ')
    tahun = models.IntegerField(default=' ')
    kontraktor = models.CharField(max_length=50, default=' E')
    surv_time = models.DateField(default=' ')
    anggaran = models.IntegerField(default=' ')
    geom = models.MultiLineStringField(srid=4326)

    
    def __unicode__(self):
        return self.lcode

    class Meta:
        verbose_name_plural = 'Drainase'

###  Pendidikan  ###
class Pendidikan(models.Model):
    namobj = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    alamat = models.CharField(max_length=50)
    jml_kelas = models.IntegerField(default=' ')
    jml_guru = models.IntegerField(default=' ')
    jml_siswa = models.IntegerField(default=' ')
    fasilitas = models.CharField(max_length=254)
    thn_bangun = models.IntegerField(default=' ')
    surveyor = models.CharField(max_length=50)
    surv_time = models.DateField()
    anggaran = models.IntegerField(default=' ')
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
        return self.namobj

    class Meta:
        verbose_name_plural = 'Pendidikan'

###  Administrasi Kabupaten Sidrap  ###
class Kab_Sidrap(models.Model):
    provinsi = models.CharField(max_length=40, default=' ')
    kecamatan = models.CharField(max_length=40, default=' ')
    desa = models.CharField(max_length=40, default=' ')
    kode2010 = models.CharField(max_length=10, default=' ')
    provno = models.CharField(max_length=2, default=' ')
    kabkotno = models.CharField(max_length=2, default=' ')
    kecno = models.CharField(max_length=3, default=' ')
    desano = models.CharField(max_length=3, default=' ')
    kabkot = models.CharField(max_length=50, default=' ')
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.provinsi

    class Meta:
        verbose_name_plural = 'Batas Administrasi'

