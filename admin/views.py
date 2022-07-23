from multiprocessing import context
from pydoc import doc
from django.shortcuts import redirect, render

from account.models import User
from .models import Doctor


def gotoAdminDashboard(request):
    return render(request, 'admin-dashboard.html')

def gotoUserlist(request):
    users = User.objects.all()

    context = {"users": users}
    return render(request, 'users.html',context)



def deleteUser(request, id):
    print(id)
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/admin/user_list/')

def gotoDoctorList(request):
    doctors = Doctor.objects.all()
    context = {"doctors":doctors}
    return render(request, 'doctor_list.html', context)

def gotoAddDoctor(request):
    return render(request, 'add_doctor.html')

def addDoctor(request):
    doctor_name = request.POST.get("doctor_name")
    sector = request.POST.get("sector")

    doctor = Doctor.objects.create(doctor_name= doctor_name, sector = sector)

    return redirect('doctor-list')

def makeAvailable(request, id):
    print(id)
    doctor = Doctor.objects.get(id=id)
    if doctor.available=='n':
        doctor.available = 'a'
    else:
        doctor.available = 'n'
    doctor.save()
    return redirect('/admin/doctor_list/')