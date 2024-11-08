from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('service-details/', views.service_details, name='service-details'),
]
