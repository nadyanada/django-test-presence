from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_form, name='attendance_form'),
    path('verify/', views.verify_view, name='verify'),
    path('success/', views.success_view, name='success'),
]