from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('create_student done')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'create_student.html',d)
