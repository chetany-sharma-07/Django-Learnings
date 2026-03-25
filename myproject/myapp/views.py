from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name='Chetany'
    age=11
    nationality='Indian'
    context={'name':name, 'age': age,'nationality': nationality}
    return render(request,'index.html',context)
