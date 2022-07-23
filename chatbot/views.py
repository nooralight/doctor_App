from multiprocessing import context
from re import L
from urllib import response
from django.shortcuts import render, redirect
from account.models import User
from admin.models import Doctor
from chatbot.models import Appointment
from .files.botResponse import getResponse
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def gotoHome(request):
    if 'user_id' not in request.session:
        response = redirect('/account/login/')               
        return response
    else:
        print(request.session['user_id'])
        user_id = request.session['user_id']
        user = User.objects.get(id = user_id)
        if user.isAdmin=='1':
            response = redirect('/admin/')
            return response
        context = {"user": user}
        return render(request, 'appointment.html', context)

def available_doctors(request):
    doctors = Doctor.objects.filter(available ='a')
    context = {"doctors":doctors}
    return render(request, "available_doctors.html", context)


def gotoChat(request):
    context = {"state":1}
    return render(request, "chatting1.html", context)

def sector(request):
    query = request.POST.get("query")
    bot_reply = getResponse(query)
    if bot_reply=="make_appointment":
        context = {"state":2}
        return render(request, "chatting1.html", context)
    else:
        response = redirect("/chatbot/chat/")
        return response

def cho_doctor(request):
    sectorCh = request.POST.get("sector")
    doctors = Doctor.objects.filter(sector=sectorCh)
    print(doctors)
    # doctor = request.POST.get("doctor")
    # datePick = request.POST.get("datePick")
    # timePick = request.POST.get("timePick")
    # res = doctor+" "+datePick+" "+timePick+" has been Connfirmed. Thank you!"
    context = {"state":3,"doctors":doctors}
    return render(request, "chatting1.html", context)

def confirming(request):
    doctor = request.POST.get("doctor")
    datePick = request.POST.get("datePick")
    timePick = request.POST.get("timePick")
    res = str(doctor)+" "+str(datePick)+" "+timePick+" has been Connfirmed. Thank you!"
    context = {"state":4}
    userID = request.session['user_id']
    user = User.objects.get(id=userID)
    user_mail = user.email
    user_name = user.fullname
    subject = 'Confirmation Email of Appointment Registration'
    message = f'Hi {user_name}, thank you for registering an Appointment in our Website. Your Appointment details is here:\nDoctor name: {doctor}, Date: {str(datePick)}, Time: {timePick} \nPlease attend at the appointment in time. Thank you!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail( subject, message, email_from, recipient_list )
    appointment = Appointment.objects.create(user_id = str(userID),doctor_name = doctor, app_date = datePick, time_book = timePick)
    return render(request, "chatting1.html",context)

def gotoAppList(request):
    userID = request.session['user_id']
    apps = Appointment.objects.filter(user_id = str(userID))
    context= {"apps":apps}
    return render(request,"appointment_list.html", context)





    
