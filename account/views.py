from pyexpat.errors import messages
from urllib import response
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from .models import User



# Create your views here.
def gotoRegistration(request):
    return render(request, 'registration.html')

def gotoLogin(request):
    return render(request, 'login.html')

def createUser(request):
    fullname = request.POST.get("fullname")
    email = request.POST.get("email")
    password  = request.POST.get("password")

    user = User.objects.create(fullname= fullname, email = email, password= password)

    return redirect('gotoLogin')

def login(request):
    input_email = request.GET.get("email")
    input_password = request.GET.get("password")

    try:
        registered_user = User.objects.get(email=input_email)
        if input_password == registered_user.password:
            print("login success")
            #return redirect('createyourshop')
            request.session['user_id'] = registered_user.id
            if registered_user.isAdmin == '1':
                response = redirect('/admin/')
                return response
            else:
                response = redirect('/')
                return response
        else:
            print("wrong password")
            return redirect('gotoLogin')
    except User.DoesNotExist:
        print("email does not exist")
        return redirect('gotoLogin')
    #return redirect('createyourshop')

def logout(request):
    request.session.flush()
    return redirect('/account/login/')