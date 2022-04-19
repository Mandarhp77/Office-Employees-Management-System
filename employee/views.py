from django.shortcuts import render, HttpResponse
from .models import employee
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        sirname = request.POST['sirname']
        salary = int(request.POST['salary'])
        location = request.POST['location']
        education = request.POST['education']
        hiring_date = request.POST['hiring_date']
        role = request.POST['role']

        new_emp = employee(name=name, sirname=sirname, salary=salary, location= location, role_id=role, education_id=education, hiring_date=hiring_date)
        new_emp.save()
        return HttpResponse("Employee Successfully Added")
    return render(request, 'register.html')

def employees(request):
    employees = employee.objects.all()
    return render(request, 'employees.html', {'employees':employees})

def remove(request, emp_id=0):
    if emp_id:
        try:
            remove_emp = employee.objects.get(id=emp_id)
            remove_emp.delete()
            return HttpResponse('Employee successfully delated')
        except:
            return HttpResponse('Enter a valid emp id')
    removes = employee.objects.all()
    return render(request, 'remove.html', {'removes':removes})

def filter(request):
    if request.method =='POST':
        name = request.POST['name']
        sirname = request.POST['sirname']
        role = request.POST['role']

        employees = employee.objects.all()
        if name:
            employees = employees.filter(name__icontains = name)
        if sirname:
            employees = employees.filter(sirname__icontains = sirname)
        if role:
            employees = employees.filter(role__name = role)

        return render(request, 'employees.html', {'employees':employees})
        
    return render(request, 'filter.html')