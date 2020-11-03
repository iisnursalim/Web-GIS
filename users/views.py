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
        'namrjl',
        'lcode',
        'spcrjl',
        'starjl',
        'utkrjl',
        'wlyrjl',
        'shp_length',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class KesehatanDeleteView(DeleteView):
    model = Kesehatan
    template_name = "maps/kesehatan_delete.html"
    success_url = "/kesehatan/"