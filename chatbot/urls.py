from django.urls import path
from . import views

urlpatterns = [
    path('' , views.gotoHome , name = 'home-page'),
    path('available/' , views.available_doctors , name = 'available'),
    path('chat/', views.gotoChat , name="goto-chat"),
    path('sector/', views.sector , name="ch-sector"),
    path('doctors/', views.cho_doctor , name="ch-doctor"),
    path('confirm/', views.confirming , name="confirm-app"),
    path('app_list/', views.gotoAppList , name="list-app")

]