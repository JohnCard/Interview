from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def hello(request):
    return render(request,'hello.html')

def user(request):
    data = {
        'first_user':Vehicle.objects.get(id=4)
    }
    return render(request,'User.html',data)