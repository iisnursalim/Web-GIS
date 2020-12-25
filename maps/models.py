from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify

# Create your models here.

###  Jalan  ###

class Jalan(models.Model):
    kelas_jln = models.CharField(max_length=250, default='')
    panjang = models.FloatField(default='')
    no_ruas = models.CharField(max_length=250, default='')
    nama_jalan = models.CharField(max_length=250, default='')
    tipe_perm = models.CharField(max_length=250, default='')
    kond_jalan = models.CharField(max_length=250, default='')
    lebar = models.FloatField(default='')
    geom = models.MultiLineStringField(srid=4326)

    def __unicode__(self):
        return self.kelas_jln

    class Meta:
        verbose_name_plural = 'Jalan'

###  Jalan Point  ###
class JalanPoint(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    nomor_ruas = models.CharField(max_length=254)
    nama_jalan = models.CharField(max_length=254)
    panjang = models.CharField(max_length=254)
    lebar = models.CharField(max_length=254)
    tpp = models.CharField(max_length=254)
    tpu = models.CharField(max_length=254)
    lhr = models.CharField(max_length=254)
    klasifikas = models.CharField(max_length=254)
    status_adm = models.CharField(max_length=254)
    tipe_permu = models.CharField(max_length=254)
    kondisi_ja = models.CharField(max_length=254)
    hambatan = models.CharField(max_length=254)
    tahun = models.CharField(max_length=254)
    anggaran = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Kondisi Jalan'

###  Jembatan  ###    
class Jembatan(models.Model):
    surveyor = models.CharField(max_length=254, default='')
    waktu_surv = models.DateField(default='')
    nama = models.CharField(max_length=254, default='')
    no_kode = models.CharField(max_length=254, default='')
    pal_km = models.CharField(max_length=254, default='')
    tipe_sebra = models.CharField(max_length=254, default='')
    jenis_jemb = models.CharField(max_length=254, default='')
    panjang = models.FloatField(default='')
    lebar = models.FloatField(default='')
    jml_bentan = models.FloatField(default='')
    kondisi = models.CharField(max_length=254, default='')
    tahun = models.CharField(max_length=254, default='')
    anggaran = models.FloatField(default='')
    sumber_dan = models.CharField(max_length=254, default='')
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Jembatan'

###  Fasilitas Kesehatan  ###
class Kesehatan(models.Model):
    surveyor = models.CharField(max_length=254, default='')
    waktu_surv = models.DateField(default='')
    nama = models.CharField(max_length=254, default='')
    alamat = models.CharField(max_length=254, default='')
    jenis = models.CharField(max_length=254, default='')
    jml_dokter = models.CharField(max_length=254, default='')
    jml_perawa = models.CharField(max_length=254, default='')
    jml_dosen = models.CharField(max_length=254, default='')
    jml_pasien = models.CharField(max_length=254, default='')
    fasilitas = models.CharField(max_length=254, default='')
    kondisi = models.CharField(max_length=254, default='')
    tahun_diba = models.CharField(max_length=254, default='')
    anggaran = models.CharField(max_length=254, default='')
    sumber_dan = models.CharField(max_length=254, default='')
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

###  Drainase  ###
class Drainase(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    no_kode = models.CharField(max_length=254)
    rpru = models.CharField(max_length=254)
    kemiringan = models.CharField(max_length=254)
    pjg_salura = models.FloatField(default='')
    lebar_salu = models.FloatField()
    kedalaman = models.FloatField()
    kondisi = models.CharField(max_length=254, )
    tahun = models.CharField(max_length=254,)
    anggaran = models.FloatField()
    sumber_dan = models.CharField(max_length=254, )
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Drainase'

###  Pendidikan  ###
class Pendidikan(models.Model):
    surveyor = models.CharField(max_length=254, default='')
    waktu_surv = models.DateField(default='')
    nama = models.CharField(max_length=254, default='')
    alamat = models.CharField(max_length=254, default='')
    jenjang = models.CharField(max_length=254, default='')
    jml_kelas = models.FloatField(default='')
    jml_guru = models.FloatField(default='')
    jml_siswa = models.FloatField(default='')
    fasilitas = models.FloatField(default='')
    tahun = models.CharField(max_length=254, default='')
    anggaran = models.FloatField(default='')
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
        return self.surveyor

    class Meta:
        verbose_name_plural = 'Pendidikan'

###  Administrasi Kabupaten Sidrap  ###
class Kab_Sidrap(models.Model):
    provinsi = models.CharField(max_length=40)
    kecamatan = models.CharField(max_length=40)
    desa = models.CharField(max_length=40)
    kode2010 = models.CharField(max_length=10)
    provno = models.CharField(max_length=2)
    kabkotno = models.CharField(max_length=2)
    kecno = models.CharField(max_length=3)
    desano = models.CharField(max_length=3)
    kabkot = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.provinsi

    class Meta:
        verbose_name_plural = 'Batas Administrasi'

