from django.shortcuts import render,redirect,get_object_or_404
from .models import contact,registration
from Appadmin.models import Teacher

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def gallery(request):
    return render(request,'Gallery.html')

def teacher(request):
    teach = Teacher.objects.all()
    return render(request,'Teachers.html',{'teac':teach})

def news(request):
    return render(request,'news.html')

def event(request):
    return render(request,'event.html')

def registrations(request):
    if request.method=='POST':
        name = request.POST['fname']
        mother_n = request.POST['mname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        religion = request.POST['religion']
        category = request.POST['category']
        place_of_birth = request.POST['pob']
        email = request.POST['email']
        M_no = request.POST['mob']
        Par_adhar = request.POST['p_adhar']
        s_adhar =request.POST['c_adhar']
        street_ad = request.POST['street']
        land_m = request.POST['landmark']
        st = request.POST['state']
        pin = request.POST['pincode']

        registration.objects.create(stud_name=name,M_name=mother_n,DOB=dob, gender=gender,religion=religion,category=category,P_O_B=place_of_birth,email=email,M_no=M_no,P_adhar=Par_adhar,C_adhar=s_adhar,street=street_ad,landmark=land_m,state=st,pin_code=pin)
        return redirect('/register')
    else:
        return render(request,'registration.html')

def contact_us(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['message']
        contact.objects.create(name=name ,email=email,phone_no=phone, message=text)
        return redirect('/contact-us')
    else:
        return render(request,'Contact-us.html')
    
# Admin Panel Functionalities:
def dash(request):
    return render(request,'Admin/dash.html')

def contacts_info(request):
    lis1 = contact.objects.all()
    return render(request,'Admin/contact-info.html',{'lis2':lis1})

def registration_info(request):
    r_lis = registration.objects.all()
    return render(request,'Admin/registration.html',{'r_lis2':r_lis})

def add_teacher(request):
    return render(request,'Admin/add_teacher.html')

def teacher_added(request):
    if request.method == 'POST':
        name = request.POST['name']
        sub = request.POST['subject']
        exp = request.POST['expertise']
        cont = request.POST['contact']
        img = request.FILES.get('image')
        Add = Teacher.objects.create(name=name ,teach_sub= sub,expertise=exp,p_no=cont,image=img )
        print(Add)
        return redirect('/add')
    else:
          return render(request,'Admin/add_teacher.html')
    
def update_T(request):
    teachers = Teacher.objects.all()
    return render(request,'Admin/added_teacher.html',{'teachers':teachers})
        
def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.teach_sub  = request.POST.get('subject')
        teacher.expertise = request.POST.get('expertise')
        teacher.p_no = request.POST.get('contact')

        if request.FILES.get('image'):
            teacher.image = request.FILES.get('image')

        teacher.save()
        return redirect('/teacher')  # change to your list view name

    return render(request, 'Admin/update_teacher.html', {'teacher': teacher})

# Delete Functionality for Contact-Us Data
def delete_contact(request, id):
    Contact = get_object_or_404(contact, id=id)
    Contact.delete()
    return redirect('/contact-details') 

# Delete Functionality for Contact-Us Data
def delete_Registrations(request, id):
    Register = get_object_or_404(registration, id=id)
    Register.delete()
    return redirect('/registration_details') 

# Delete Functionality for Added Teacher in Database
def delete_teacher(request, id):
    T = get_object_or_404(Teacher, id=id)
    T.delete()
    return redirect('/teacher') 
