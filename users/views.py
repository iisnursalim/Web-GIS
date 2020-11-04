from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
from maps.models import (
    Jalan,
    Jembatan,
    Kesehatan,
    Drainase,
    Pendidikan,
    Kab_Sidrap
)
from .forms import (
    UserRegisterForm,
    JalanForm,
    JembatanForm,
    KesehatanForm,
    DrainaseForm,
    PendidikanForm,
    Kab_SidrapForm
)

# Register-->
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Jalan-->
# List-->
def JalanListView(request):
    jalan = Jalan.objects.all()
    return render(request,'maps/jalan_list.html',{'jalan':jalan})
# Upload-->
def uploadjalan(request):
    jalanform = JalanForm()
    if request.method == "POST":
        jalanform = JalanForm(request.POST)
        if jalanform.is_valid():
            print(jalanform.cleaned_data)
            Jalan.objects.create(**jalanform.cleaned_data)
            return redirect('/')
        else:
            print(jalanform.errors)
    context = {
            "form": jalanform
        }
    return render(request,'upload/upload_jalan.html', context)
# Update Attribute-->
class JalanAttrUpdateView(UpdateView):
    model = Jalan
    fields = [
        'surveyor',
        'surv_time',
        'number',
        'name',
        'length_km',
        'width_m',
        'tpp',
        'tpu',
        'lhr',
        'status',
        'surf_type',
        'kondisi',
        'hambatan', 
        'tahun',
        'anggaran',
        'tipe_ruas',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class JalanDeleteView(DeleteView):
    model = Jalan
    template_name = "maps/jalan_delete.html"
    success_url = "/street/"


# Jembatan-->
# List-->
def JembatanListView(request):
    jembatan = Jembatan.objects.all()
    return render(request,'maps/jembatan_list.html',{'jembatan':jembatan})
# Upload-->
def uploadjembatan(request):
    jembatanform = JembatanForm()
    if request.method == "POST":
        jembatanform = JembatanForm(request.POST)
        if jembatanform.is_valid():
            print(jembatanform.cleaned_data)
            Jembatan.objects.create(**jembatanform.cleaned_data)
            return redirect('/')
        else:
            print(jembatanform.errors)
    context = {
            "form": jembatanform
        }
    return render(request,'upload/upload_jembatan.html', context)
# Update Attribute-->
class JembatanAttrUpdateView(UpdateView):
    model = Jembatan
    fields = [
        'surveyor',
        'surv_date',
        'nama',
        'pal_km',
        'panjang_m',
        'lebar_m',
        'bentang',
        'tipe_jem',
        'penyebrang',
        'bhn_konstr',
        'kondisi',
        'tahun',
        'anggaran',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class JembatanDeleteView(DeleteView):
    model = Jembatan
    template_name = "maps/jembatan_delete.html"
    success_url = "/jembatan/"


# Fasilitas Kesehatan-->
# List-->
def KesehatanListView(request):
    kesehatan = Kesehatan.objects.all()
    return render(request,'maps/kesehatan_list.html',{'kesehatan':kesehatan})
# Upload-->
def uploadkesehatan(request):
    kesehatanform = KesehatanForm()
    if request.method == "POST":
        kesehatanform = KesehatanForm(request.POST)
        if kesehatanform.is_valid():
            print(kesehatanform.cleaned_data)
            Kesehatan.objects.create(**kesehatanform.cleaned_data)
            return redirect('/')
        else:
            print(kesehatanform.errors)
    context = {
            "form": kesehatanform
        }
    return render(request,'upload/upload_Kesehatan.html', context)
# Update Attribute-->
class KesehatanAttrUpdateView(UpdateView):
    model = Kesehatan
    fields = [
        'namobj',
        'alamat',
        'remark',
        'jml_dktr',
        'jml_prwt',
        'jml_pasien',
        'jml_ruang',
        'fasilitas',
        'kond_bgnn',
        'tahun',
        'anggaran',
        'sumb_dana',
        'kontraktor',
        'surv_time',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class KesehatanDeleteView(DeleteView):
    model = Kesehatan
    template_name = "maps/kesehatan_delete.html"
    success_url = "/kesehatan/"


# Drainase-->
# List-->
def DrainaseListView(request):
    drainase = Drainase.objects.all()
    return render(request,'maps/drainase_list.html',{'drainase':drainase})
# Upload-->
def uploaddrainase(request):
    drainaseform = DrainaseForm()
    if request.method == "POST":
        drainaseform = DrainaseForm(request.POST)
        if drainaseform.is_valid():
            print(drainaseform.cleaned_data)
            Drainase.objects.create(**drainaseform.cleaned_data)
            return redirect('/')
        else:
            print(drainaseform.errors)
    context = {
            "form": drainaseform
        }
    return render(request,'upload/upload_Drainase.html', context)
# Update Attribute-->
class DrainaseAttrUpdateView(UpdateView):
    model = Drainase
    fields = [
        'lcode',
        'rpru',
        'kemiringan',
        'panjang_m',
        'kdlmn_m',
        'kondisi',
        'tahun',
        'anggaran',
        'kontraktor',
        'surv_time',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class DrainaseDeleteView(DeleteView):
    model = Drainase
    template_name = "maps/drainase_delete.html"
    success_url = "/drainase/"


# Pendidikan-->
# List-->
def PendidikanListView(request):
    pendidikan = Pendidikan.objects.all()
    return render(request,'maps/pendidikan_list.html',{'pendidikan':pendidikan})
# Upload-->
def uploadpendidikan(request):
    pendidikanform = PendidikanForm()
    if request.method == "POST":
        pendidikanform = PendidikanForm(request.POST)
        if pendidikanform.is_valid():
            print(pendidikanform.cleaned_data)
            Pendidikan.objects.create(**pendidikanform.cleaned_data)
            return redirect('/')
        else:
            print(pendidikanform.errors)
    context = {
            "form": pendidikanform
        }
    return render(request,'upload/upload_Pendidikan.html', context)
# Update Attribute-->
class PendidikanAttrUpdateView(UpdateView):
    model = Pendidikan
    fields = [
        'namobj',
        'remark',
        'alamat',
        'jml_kelas',
        'jml_guru',
        'jml_siswa',
        'fasilitas',
        'thn_bangun',
        'anggaran',
        'surveyor',
        'surv_time',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class PendidikanDeleteView(DeleteView):
    model = Pendidikan
    template_name = "maps/pendidikan_delete.html"
    success_url = "/pendidikan/"


# Administrasi Kabupaten Sidrap-->
# List-->
def Kab_SidrapListView(request):
    kab_sidrap = Kab_Sidrap.objects.all()
    return render(request,'maps/kab_sidrap_list.html',{'kab_sidrap':kab_sidrap})
# Upload-->
def uploadkab_sidrap(request):
    kab_sidrapform = Kab_SidrapForm()
    if request.method == "POST":
        kab_sidrapform = Kab_SidrapForm(request.POST)
        if kab_sidrapform.is_valid():
            print(kab_sidrapform.cleaned_data)
            Kab_Sidrap.objects.create(**kab_sidrapform.cleaned_data)
            return redirect('/')
        else:
            print(kab_sidrapform.errors)
    context = {
            "form": kab_sidrapform
        }
    return render(request,'upload/upload_Kab_Sidrap.html', context)
# Update Attribute-->
class Kab_SidrapAttrUpdateView(UpdateView):
    model = Kab_Sidrap
    fields = [
        'Provinsi',
        'Kecamatan',
        'Desa',
        'Kabupaten',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class Kab_SidrapDeleteView(DeleteView):
    model = Kab_Sidrap
    template_name = "maps/kab_sidrap_delete.html"
    success_url = "/pkab_sidrap/"