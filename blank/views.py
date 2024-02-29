from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

countries = ('Poland', 'Czechia', 'Slovakia')

def index(request):
    return render(request, 'index.html')

def show_list(request):
    # countries = ('USA','Germany', 'France')
    # context = {'countries' : contries}
    template1 = loader.get_template('base.html')
    return HttpResponse(template1.render())

def not_implemented(request):
    return HttpResponse(f'not_implemented, request: path{request.path} method:{request.method}' )

def simple(request):
    ii=10
    return render(request, 'simple.html')

def ttt(request):
    return HttpResponse('this is ttt(request) aaa')

def countries(request):
    return render(request, 'countries.html', {'countries' : countries})
