from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Employees
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import EmployeesForm
from django.contrib import messages


# Create your views here.
def show_all(request):
    employees = Employees.objects.all()
    return render(request,'all.html',{'employees':employees})

def show_all_api(request):
    employees = Employees.objects.all()
    employeesjson = serializers.serialize('json', employees)
    return HttpResponse(employeesjson, content_type="text/json-comment-filtered")

@csrf_exempt
def query(request):
    message = 'Enter ID'
    if request.method == 'POST':
        employeeid = request.POST['employeeid']
        try:
            employee = Employees.objects.get(pk=employeeid)
            return render(request, 'query.html', {'employee': employee})
        except ObjectDoesNotExist:
            message = "This ID doesn't exist"
            return render(request, 'query.html', {'message': message})
    return render(request, 'query.html',{'message':message})

def query_api(request):
    employeeid = request.GET['employeeid']
    employee = Employees.objects.filter(pk=employeeid)
    if employee.exists():
        employeejson = serializers.serialize('json', employee)
    else:
        employeejson = "This ID doesn't exist"
    return HttpResponse(employeejson, content_type="text/json-comment-filtered")

def add(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('add')
    employees = Employees.objects.all()
    return render(request, 'add.html', {'employees': employees})

def delete(request):
    message = 'Enter ID'
    employees = Employees.objects.all()
    if request.method == 'POST':
        employeeid = request.POST['employeeid']
        try:
            employee = Employees.objects.get(pk=employeeid)
            employee.delete()
            return redirect('delete')
        except ObjectDoesNotExist:
            message = "This ID doesn't exist"
            return render(request, 'delete.html', {'message': message, 'employees':employees})
    return render(request, 'delete.html', {'message': message, 'employees':employees})


def update(request):
    message = 'Enter ID'
    employees = Employees.objects.all()
    if request.method == 'POST':
        employeeid = request.POST['employeeid']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        birthdate = request.POST['birthdate']
        try:
            employee = Employees.objects.get(pk=employeeid)
            if lastname == '':
                lastname = employee.lastname
            if firstname == '':
                firstname = employee.firstname
            if birthdate == '':
                birthdate = employee.birthdate
            Employees.objects.filter(pk=employeeid).update(lastname=lastname, firstname=firstname, birthdate=birthdate)
            return redirect('update')
        except ObjectDoesNotExist:
            message = "This ID doesn't exist"
            return render(request, 'update.html', {'message': message, 'employees':employees})
    return render(request, 'update.html', {'message': message, 'employees':employees})



