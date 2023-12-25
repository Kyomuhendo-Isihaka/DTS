from django.shortcuts import render
from dts.models import HealthCenter

# Create your views here.
def login(request):
    healthcenters = HealthCenter.objects.all()
    context = {
        'healthcenters':healthcenters
    }

    return render(request, 'login_.html', context)

def main(request):
    return render(request, 'layout_.html')