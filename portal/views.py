from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact,currentevents,links,news,Register

# Create your views here.
def home(request):
    pdflink =currentevents.objects.all()
    implink = links.objects.all()
    newsevent = news.objects.all()
    params ={'pdflink':pdflink,'implink':implink ,'news':newsevent}
    return render(request,'portal/home.html',params)

def contact(request):
    thank= False
    if request.method =="POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        content = request.POST.get('content','')
        if len(name)<3 or len(phone)<10 or len(email)<12 or len(content)<5:
            messages.error(request,'Please Fill the form correctly!')
        else:
            contact =Contact(name=name,content=content,phone=phone,email=email)
            contact.save()
            messages.success(request,'we Will contact you soon...')
    return render(request,'portal/contact.html')

def faq(request):
    return render(request,'portal/faqs.html')


def about(request):
    return render(request,'portal/about.html')


def admitview(request):
    return render(request,'loginmodule/admitcard.html')

def register(request):
    return render(request,'updates/register.html')

def registerview(request):
    return render(request,'updates/registerview.html')


def instruction(request):
    return render(request,'updates/instruction.html')

def payment(request):
    return render(request,'updates/payment.html')

def resultdisplay(request):
    return render(request,'loginmodule/result.html')

def result1(request):
    return render(request,'updates/result1.html')

def profile(request):
    return render(request,'loginmodule/profile.html')

def dashboard(request):
    resp =request.session.get('resp')
    
    print(resp)    
    return render(request,'updates/dashboard.html')

def handleregister(request):
    if request.method== "POST":
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        fathername = request.POST.get('fathername','')
        mothername = request.POST.get('mothername','')
        gender = request.POST.get('gender','')
        DOB = request.POST.get('DOB','')
        address1 = request.POST.get('address1','')
        address2 = request.POST.get('address2','')
        country = request.POST.get('country','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        district = request.POST.get('district','')
        phone = request.POST.get('phone','')
        pincode = request.POST.get('pincode','')
        email = request.POST.get('email','')
        email1 = request.POST.get('email1','')
        pass1 = request.POST.get('pass1','')
        pass2 = request.POST.get('pass2','')
        # checks
        if len(phone)<10:
            messages.error(request,'Your phone must be atleast 10 digits')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request,"Your password doesn't match")
            return redirect('home')
        if email != email1:
            messages.error(request,"Your emailid doesn't match")
            return redirect('home')
        existuser = User.objects.all()
        for item in existuser:
            if item.username == phone:
                messages.error(request,'Try different phone no. ')
                return redirect('home')

        # create user

        createUser = User.objects.create_user(phone,email,pass1)
        createUser.first_name = fname
        createUser.last_name = lname
        createUser.save()

        registerUser =Register(fname=fname,lname=lname,fathername=fathername,mothername=mothername,gender=gender,DOB=DOB,address1=address1,address2=address2,country=country,city=city,state=state,district=district,phone=phone,pincode=pincode,email=email,pass1=pass1)
        registerUser.save()
        messages.success(request,'You has been registered successfully ')
        return redirect('home')
    else:
        return HttpResponse('404 not found')

def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username =loginusername,password =loginpassword)

        if user is not None:
            username= loginusername
            login(request,user)
            messages.success(request,'You has been successfully logged In')
            request.session['resp'] = username
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('register')
    return HttpResponse('404 not found')

def handlelogout(request):
    logout(request)
    messages.success(request,'You has been successfully logged out')
    return redirect('home')

def handleimage(request):
    if request.method == "POST":
        tenmark = request.POST.get('tenmark','')
        twmark = request.POST.get('twmark','')
        bmark = request.POST.get('bmark','')
        bcertificate = request.POST.get('bcertificate','')
        ccertificate = request.POST.get('ccertificate','')
        gmark = request.POST.get('gmark','')
        smark = request.POST.get('smark','')
        sign = request.POST.get('sign','')
        photo = request.POST.get('  photo')
        gmark = request.POST.get('gmark','')
        
        return redirect('payment')

        
        
    else:
        return HttpResponse('404 not found')






def registerview(request):
    return render(request,'updates/registerview.html')


def application(request):
        return render(request,'updates/application.html')
    