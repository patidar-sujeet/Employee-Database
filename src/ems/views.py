# from http.client import HTTPResponse

from django.http import Http404
from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, 'ems/home.html',{'employees':employees})
    # return HttpResponse('Hello, World!')

def employee_details(request, employee_id):
    # return HttpResponse(f'<p>employee_details view with id {employee_id}</p>')
    try:

        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found')

    return render(request,'ems/employee_details.html',{'employee':employee})
