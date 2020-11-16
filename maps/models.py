from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify

# Create your models here.

###  Jalan  ###

class Jalan(models.Model):
    kelas_jln = models.CharField(max_length=250)
    panjang = models.FloatField()
    no_ruas = models.CharField(max_length=250)
    nama_jalan = models.CharField(max_length=250)
    tipe_perm = models.CharField(max_length=250)
    kond_jalan = models.CharField(max_length=250)
    lebar = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    def __unicode__(self):
        return self.nama_jalan

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
        return self.nama_jalan

    class Meta:
        verbose_name_plural = 'Kondisi Jalan'

###  Jembatan  ###    
class Jembatan(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    nama = models.CharField(max_length=254)
    no_kode = models.CharField(max_length=254)
    pal_km = models.CharField(max_length=254)
    tipe_sebra = models.CharField(max_length=254)
    jenis_jemb = models.CharField(max_length=254)
    panjang = models.FloatField()
    lebar = models.FloatField()
    jml_bentan = models.FloatField()
    kondisi = models.CharField(max_length=254)
    tahun = models.CharField(max_length=254)
    anggaran = models.FloatField()
    sumber_dan = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Jembatan'

###  Fasilitas Kesehatan  ###
class Kesehatan(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    nama = models.CharField(max_length=254)
    alamat = models.CharField(max_length=254)
    jenis = models.CharField(max_length=254)
    jml_dokter = models.CharField(max_length=254)
    jml_perawa = models.CharField(max_length=254)
    jml_dosen = models.CharField(max_length=254)
    jml_pasien = models.CharField(max_length=254)
    fasilitas = models.CharField(max_length=254)
    kondisi = models.CharField(max_length=254)
    tahun_diba = models.CharField(max_length=254)
    anggaran = models.CharField(max_length=254)
    sumber_dan = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

###  Drainase  ###
class Drainase(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    no_kode = models.CharField(max_length=254)
    rpru = models.CharField(max_length=254)
    kemiringan = models.CharField(max_length=254)
    pjg_salura = models.FloatField()
    lebar_salu = models.FloatField()
    kedalaman = models.FloatField()
    kondisi = models.CharField(max_length=254)
    tahun = models.CharField(max_length=254)
    anggaran = models.FloatField()
    sumber_dan = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
        return self.no_kode

    class Meta:
        verbose_name_plural = 'Drainase'

###  Pendidikan  ###
class Pendidikan(models.Model):
    surveyor = models.CharField(max_length=254)
    waktu_surv = models.DateField()
    nama = models.CharField(max_length=254)
    alamat = models.CharField(max_length=254)
    jenjang = models.CharField(max_length=254)
    jml_kelas = models.FloatField()
    jml_guru = models.FloatField()
    jml_siswa = models.FloatField()
    fasilitas = models.FloatField()
    tahun = models.CharField(max_length=254)
    anggaran = models.FloatField()
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
        return self.nama

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

