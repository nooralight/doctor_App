from django.urls import path
from . import views


urlpatterns = [
    path('', views.gotoAdminDashboard, name="admin-dashboard"),
    path('user_list/', views.gotoUserlist, name="user-list"),
    path('delete_user/<str:id>/', views.deleteUser, name="delete-user"),
    path('doctor_list/', views.gotoDoctorList, name="doctor-list"),
    path('<str:id>/make_available', views.makeAvailable, name="make-available"),
    path('doctor_add/', views.gotoAddDoctor, name="add-doctorPage"),
    path('adding_doctor', views.addDoctor, name="doctor-adding"),
]