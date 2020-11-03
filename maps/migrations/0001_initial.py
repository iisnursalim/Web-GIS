# Generated by Django 3.0.8 on 2020-07-19 10:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drainase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kode_Drainase', models.CharField(max_length=50)),
                ('Ruas_Pangkal_Ruas_Ujung', models.CharField(max_length=100)),
                ('Kemiringan_Derajat', models.IntegerField()),
                ('Panjang_Saluran_m', models.IntegerField()),
                ('Kedalaman_Saluran_m', models.IntegerField()),
                ('Kondisi_Drainase', models.CharField(max_length=50)),
                ('Tahun_Pembuatan', models.IntegerField()),
                ('Anggaran_yang_digunakan', models.BigIntegerField()),
                ('Perusahaan_atau_Kontraktor_yang_membangun', models.CharField(max_length=50)),
                ('Tanggal_Survey', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Drainase',
            },
        ),
        migrations.CreateModel(
            name='Jalan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surveyor', models.CharField(max_length=250)),
                ('Waktu_Survey', models.DateField()),
                ('Nomor_Ruas', models.IntegerField()),
                ('Nama_Ruas', models.CharField(max_length=250)),
                ('Panjang_Ruas_km', models.BigIntegerField()),
                ('Lebar_Jalan_m', models.BigIntegerField()),
                ('Titik_Pengenal_Pangkal', models.CharField(max_length=250)),
                ('Titik_Pengenal_Ujung', models.CharField(max_length=250)),
                ('Lalu_Lintas_Harian_Ratarata', models.IntegerField()),
                ('Status_Administrasi', models.CharField(max_length=100)),
                ('Tipe_Permukaan_Jalan', models.CharField(max_length=100)),
                ('Kondisi_Jalan', models.CharField(max_length=100)),
                ('Hambatan_Lalu_Lintas', models.CharField(max_length=100)),
                ('Tahun_Pekerjaan', models.IntegerField()),
                ('Anggaran_Pekerjaan', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Jalan',
            },
        ),
        migrations.CreateModel(
            name='Jembatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surveyor', models.CharField(max_length=100)),
                ('Tanggal_Survey', models.DateField()),
                ('Nama_Jembatan', models.CharField(max_length=100)),
                ('PAL_Kilometer', models.IntegerField()),
                ('Tipe_Penyeberangan', models.CharField(max_length=100)),
                ('Panjang_Jembatan_m', models.BigIntegerField()),
                ('Lebar_Jalur_m', models.BigIntegerField()),
                ('Jumlah_Bentang', models.IntegerField()),
                ('Tipe_Jembatan', models.CharField(max_length=100)),
                ('Bahan_Konstruksi_Utama', models.CharField(max_length=50)),
                ('Kondisi', models.CharField(max_length=100)),
                ('Tahun_Pekerjaan', models.IntegerField()),
                ('Biaya_Pekerjaan', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Jembatan',
            },
        ),
        migrations.CreateModel(
            name='Kab_Sidrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Provinsi', models.CharField(max_length=40)),
                ('Kecamatan', models.CharField(max_length=40)),
                ('Desa', models.CharField(max_length=40)),
                ('Kabupaten', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Batas Administrasi',
            },
        ),
        migrations.CreateModel(
            name='Kesehatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Fasilitas_Kesehatan', models.CharField(max_length=250)),
                ('Alamat', models.CharField(max_length=250)),
                ('Jenis_Fasilitas_Kesehatan', models.CharField(max_length=250)),
                ('Jumlah_Dokter', models.IntegerField()),
                ('Jumlah_Perawat', models.IntegerField()),
                ('Jumlah_Pasien_per_tahun', models.IntegerField()),
                ('Jumlah_Ruangan', models.IntegerField()),
                ('Fasilitas_yang_tersedia', models.CharField(max_length=250)),
                ('Kondisi_Bangunan', models.CharField(max_length=100)),
                ('Tahun_Dibangun', models.IntegerField()),
                ('Anggaran_Pembangunan', models.BigIntegerField()),
                ('Sumber_Dana', models.CharField(max_length=50)),
                ('Perusahaan_atau_Kontraktor_yang_membangun', models.CharField(max_length=100)),
                ('Waktu_Survey', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Fasilitas Kesehatan',
            },
        ),
    ]