from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Jalan(models.Model):
    Surveyor = models.CharField(max_length=250)
    Waktu_Survey = models.DateField()
    Nomor_Ruas = models.IntegerField()
    Nama_Ruas = models.CharField(max_length=250)
    Panjang_Ruas_km = models.BigIntegerField()
    Lebar_Jalan_m = models.BigIntegerField()
    Titik_Pengenal_Pangkal = models.CharField(max_length=250)
    Titik_Pengenal_Ujung = models.CharField(max_length=250)
    Lalu_Lintas_Harian_Ratarata = models.IntegerField()
    Status_Administrasi = models.CharField(max_length=100)
    Tipe_Permukaan_Jalan = models.CharField(max_length=100)
    Kondisi_Jalan = models.CharField(max_length=100)
    Hambatan_Lalu_Lintas = models.CharField(max_length=100)
    Tahun_Pekerjaan = models.IntegerField()
    Anggaran_Pekerjaan = models.BigIntegerField()
    geom = models.LineStringField(srid=4326)

    def __unicode__(self):
        return self.Surveyor

    class Meta:
        verbose_name_plural = 'Jalan'
    
class Jembatan(models.Model):
    Surveyor = models.CharField(max_length=100)
    Tanggal_Survey = models.DateField()
    Nama_Jembatan = models.CharField(max_length=100)
    PAL_Kilometer = models.IntegerField()
    Tipe_Penyeberangan = models.CharField(max_length=100)
    Panjang_Jembatan_m = models.BigIntegerField()
    Lebar_Jalur_m = models.BigIntegerField()
    Jumlah_Bentang = models.IntegerField()
    Tipe_Jembatan = models.CharField(max_length=100)
    Bahan_Konstruksi_Utama = models.CharField(max_length=50)
    Kondisi = models.CharField(max_length=100)
    Tahun_Pekerjaan = models.IntegerField()
    Biaya_Pekerjaan = models.BigIntegerField()
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.Surveyor

    class Meta:
        verbose_name_plural = 'Jembatan'

class Kesehatan(models.Model):
    Nama_Fasilitas_Kesehatan = models.CharField(max_length=250)
    Alamat = models.CharField(max_length=250)
    Jenis_Fasilitas_Kesehatan = models.CharField(max_length=250)
    Jumlah_Dokter = models.IntegerField()
    Jumlah_Perawat = models.IntegerField()
    Jumlah_Pasien_per_tahun = models.IntegerField()
    Jumlah_Ruangan = models.IntegerField()
    Fasilitas_yang_tersedia = models.CharField(max_length=250)
    Kondisi_Bangunan = models.CharField(max_length=100)
    Tahun_Dibangun = models.IntegerField()
    Anggaran_Pembangunan = models.BigIntegerField()
    Sumber_Dana = models.CharField(max_length=50)
    Perusahaan_atau_Kontraktor_yang_membangun = models.CharField(max_length=100)
    Waktu_Survey = models.DateField()
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.Nama_Fasilitas_Kesehatan

    class Meta:
        verbose_name_plural = 'Fasilitas Kesehatan'

class Drainase(models.Model):
    Kode_Drainase = models.CharField(max_length=50)
    Ruas_Pangkal_Ruas_Ujung = models.CharField(max_length=100)
    Kemiringan_Derajat = models.IntegerField()
    Panjang_Saluran_m = models.IntegerField()
    Kedalaman_Saluran_m = models.IntegerField()
    Kondisi_Drainase = models.CharField(max_length=50)
    Tahun_Pembuatan = models.IntegerField()
    Anggaran_yang_digunakan = models.BigIntegerField()
    Perusahaan_atau_Kontraktor_yang_membangun = models.CharField(max_length=50)
    Tanggal_Survey = models.DateField()
    geom = models.LineStringField(srid=4326)
    
    def __unicode__(self):
        return self.Kode_Drainase

    class Meta:
        verbose_name_plural = 'Drainase'

class Kab_Sidrap(models.Model):
    Provinsi = models.CharField(max_length=40)
    Kecamatan = models.CharField(max_length=40)
    Desa = models.CharField(max_length=40)
    Kabupaten = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.Kecamatan

    class Meta:
        verbose_name_plural = 'Batas Administrasi'

