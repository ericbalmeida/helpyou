from django.shortcuts import render
from django.http import HttpResponse

def conversas(request):
    return render(request, 'helpyou/conversas.html')