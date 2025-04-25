"""
URL configuration for govind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about-us'),
    path('gallery',views.gallery,name='gallery'),
    path('event',views.event,name='event'),
    path('teacher',views.teacher,name='teacher'),
    path('news',views.news,name='news'),
    path('register',views.registrations,name='registration'),
    path('contact-us',views.contact_us,name='contact-us'),
    path('contact-details',views.contacts_info, name='contact-detail'),
    path('registration_details',views.registration_info, name='registration-detail'),
    path('delete_contact/<int:id>',views.delete_contact, name='delete_contact'),
    path('delete_register/<int:id>',views.delete_Registrations, name='delete_register'),
    path('add_teacher',views.add_teacher, name='add_teacher'),
    path('add',views.teacher_added, name='add'),
    path('update_teacher', views.update_T, name='update_T'),
    path('update/<int:pk>', views.update_teacher, name='update_teacher'),
     path('delete_teacher/<int:id>',views.delete_teacher, name='delete_teacher'),
     path('dashboard',views.dash, name='dashboard'),
]
