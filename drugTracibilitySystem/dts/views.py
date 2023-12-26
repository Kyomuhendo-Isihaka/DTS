from django.shortcuts import render, redirect,get_object_or_404
from . import models

# Create your views here.
def home(request):
    return render(request, 'index.html')

def administrators(request):
    return render(request, 'pages/administrators.html')

def transactions(request):
    return render(request, 'pages/transactions.html')

def pharmaceuticals(request):
    drugs = models.Drug.objects.all().order_by('-DrugID')

    if request.method=="POST":
        drug_name = request.POST.get('drug_name')
        batch_num = request.POST.get('batch_num')
        drug_des = request.POST.get('drug_description')
        expirationDate = request.POST.get('expirationDate')
        quantity = request.POST.get('drug_quantity')

        drug = models.Drug(DrugName = drug_name, BatchNumber=batch_num, DrugDescription=drug_des, ExpirationDate=expirationDate, Quantity = quantity)
        drug.save()

    context={
        'drugs':drugs,
    }
    return render(request, 'pages/pharmaceuticals.html', context)

def editpharmaceutical(request, pk):
    drug = get_object_or_404(models.Drug, DrugID=pk)
    print(drug)
    if request.method=="POST":
        drug_name = request.POST.get('drug_name')
        batch_num = request.POST.get('batch_num')
        drug_des = request.POST.get('drug_description')
        quantity = request.POST.get('drug_quantity')
        
        drug.DrugName=drug_name
        drug.BatchNumber=batch_num
        drug.DrugDescription=drug_des
        drug.Quantity = quantity

        drug.save()
    return redirect('pharmaceuticals')

def deletePharmaceutical(request, pk):
    drug = get_object_or_404(models.Drug, DrugID=pk)
    drug.delete()
    return redirect('pharmaceuticals')

def healthcenters(request):
    msg = ''
    healthcenters= models.HealthCenter.objects.all().order_by('-id')
   
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
