from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee

# Create your views here.


def index(request):
    myEmployees = Employee.objects.all().values()
    # output = ''
    # for x in myEmployees:
    #     output += x['name']
    template = loader.get_template('index.html')
    context = {
        'myEmployees': myEmployees
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({}, request))

def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['title']
    newEmployee = Employee(name=data1, title=data2)
    newEmployee.save()
    return HttpResponseRedirect(reverse('index'))