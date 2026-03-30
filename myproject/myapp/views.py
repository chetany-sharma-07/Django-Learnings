from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name='Chetany'
    age=11
    nationality='Indian'
    context={'name':name, 'age': age,'nationality': nationality}
    return render(request,'index.html')

def counter(request):
    text=request.GET['text']
    amount_of_words=len(text.split(" "))
    return render(request, 'counter.html',{'amount': amount_of_words})

