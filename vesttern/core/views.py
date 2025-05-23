from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def development(request):
    return render(request, 'core/development.html')

def support(request):
    return render(request, 'core/support.html')

def replication(request):
    return render(request, 'core/replication.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')


