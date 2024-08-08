from django.shortcuts import render, redirect
from django.views import View
from departments.models import DepartmentHeads
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication/login')
def index(request):
    if request.user.is_superuser:
        # Admin profile view
        user = request.user
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        return render(request, 'dashboard/indexAdmin.html', context)
    else:
        user  = request.user

        department_head = DepartmentHeads.objects.get(head=user)
        department_name = department_head.department.name
        contactNo = department_head.contact_no        


        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'department_name' : department_name,
            'contactNo' : contactNo
        }
        return render(request, 'dashboard/index.html', context)

