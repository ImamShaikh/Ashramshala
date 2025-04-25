from django.shortcuts import render,redirect
from school.models import contact

# Create your views here.
def home(request):
    return render(request,'Admin/first.html')

def contacts_info(request):
    lis1 = contact.objects.all()
    return render(request,'Admin/contact-info.html',{"lis2":lis1})
