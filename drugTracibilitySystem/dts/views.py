from django.shortcuts import render, redirect,get_object_or_404
from . import models

# Create your views here.
def home(request):
    return render(request, 'index.html')


def transactions(request):
    return render(request, 'pages/transactions.html')

def pharmaceuticals(request):
    return render(request, 'pages/pharmaceuticals.html')

def healthcenters(request):
    msg = ''
    healthcenters= models.HealthCenter.objects.all()
   

    if request.method=='POST':
        hlthc_name = request.POST.get('healthcenter')
        district = request.POST.get('district')
        village = request.POST.get('village')

        healthcenter = models.HealthCenter(healthcenter_name=hlthc_name, district=district, village=village)
        healthcenter.save()
        msg = "Added Successfully"
        
   
    context = {
        'msg':msg,
        'healthcenters':healthcenters,
    }

    return render(request, 'pages/healthcenters.html', context)

def edithealthcenter(request, pk):
    healthcenter = get_object_or_404(models.HealthCenter, pk=pk)
    if request.method=='POST':
        hlthc_name = request.POST.get('healthcenter')
        district = request.POST.get('district')
        village = request.POST.get('village')

        healthcenter.healthcenter_name = hlthc_name
        healthcenter.district = district
        healthcenter.village = village
        
        healthcenter.save()
        msg='Updated Successfully'
    return redirect('healthcenters')

def healthcenter(request, pk):
    healthcenter = get_object_or_404(models.HealthCenter, pk=pk)

    context={
        'healthcenter':healthcenter,
    }
    return render (request, 'pages/healthcenter.html', context)

def deleteHealthcenter(request, pk):
    healthcenter = get_object_or_404(models.HealthCenter, pk= pk)
    healthcenter.delete()
    return redirect('healthcenters')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')
