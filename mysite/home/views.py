from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.shortcuts import render,redirect
from .models import certi
from django.db import connection
from django.http import HttpResponse
from .forms import certiform
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import OrdersForm


def favicon(request):
    return HttpResponse(status=204)  # Return an empty response with status code 204 (No Content)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials..!!")
    return render(request, 'login.html')

@login_required(login_url= '/login/')
def contact(request):
    try:
        contact = Contact.objects.get(staff=request.user)
    except Contact.DoesNotExist:
        contact = None
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        branch = request.POST.get('branch')
        stdyear = request.POST.get('stdyear')
        phno = request.POST.get('phno')
        git = request.POST.get('git')
        linkedin = request.POST.get('linkedin')
        hrank = request.POST.get('hrank')
        aadhar = request.POST.get('aadhar')
        addr = request.POST.get('addr')
        adnum = request.POST.get('adnum')
        #contact = Contact.objects.create(staff=request.user,fullname=fullname,branch=branch,stdyear=stdyear,phno=phno,git=git,linkedin=linkedin,hrank=hrank,aadhar=aadhar,addr=addr,adnum=adnum)
        if contact:  # If contact exists, update it
            contact.fullname = fullname
            contact.branch = branch
            contact.stdyear = stdyear
            contact.phno = phno
            contact.git = git
            contact.linkedin = linkedin
            contact.hrank = hrank
            contact.aadhar = aadhar
            contact.addr = addr
            contact.adnum = adnum
            contact.save()
        else:  # If contact doesn't exist, create a new one
            contact = Contact.objects.create(
                staff=request.user,
                fullname=fullname,
                branch=branch,
                stdyear=stdyear,
                phno=phno,
                git=git,
                linkedin=linkedin,
                hrank=hrank,
                aadhar=aadhar,
                addr=addr,
                adnum=adnum
            )
        return redirect('profile')
    return render(request,'contact.html')

#def save_internships_and_certifications(request):
#    if request.method == 'POST':return render(request, 'contact.html')
def orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders.html')  # Redirect to a success page
    else:
        form = OrdersForm()
    return render(request, 'orders.html', {'form': form})


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("password doesn't match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url= '/login/')
def student1(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render(request,'student1.html',context)


@login_required(login_url= '/login/')
def studentdetail(request,pk):
    try:
            workers = User.objects.get(id=pk)
            contact = Contact.objects.get(staff=workers)
    except User.DoesNotExist:
            # Handle the case where the user is not found
        return render(request, 'user_not_found.html')
    except Contact.DoesNotExist:
            # Handle the case where the contact is not found
        contact = None

    context = {
        'workers': workers,
        'contact': contact,
    }
    return render(request, 'studentdetail.html', context)


@login_required(login_url= '/login/')
def certi(request):
    #items = certi.objects.all()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM home_certi')
        items = cursor.fetchall()
    print(items)
    if request.method =='POST':
        form = certiform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certi')
    else:
        form = certiform()
    context={
        'items':items,
        'form':form,
    }
    return render(request,'certi.html',context)

@login_required(login_url= '/login/')
def certidel(request, pk):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM home_certi WHERE id = %s', [pk])
        item = cursor.fetchone()
    if not item:
        # Handle the case where the item is not found
        return HttpResponse(status=404)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM home_certi WHERE id = %s', [pk])
        return redirect('certi')
    return render(request, 'certidel.html', {'item': item})

@login_required(login_url= '/login/')
def certiupdate(request, pk):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM home_certi WHERE id = %s', [pk])
        item = cursor.fetchone()

    if not item:
        return HttpResponse(status=404)

    if request.method == 'POST':
        form = certiform(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute('UPDATE home_certi SET type=%s,credits=%s,name = %s, score = %s, level = %s, adnum = %s, image = %s WHERE id = %s',
                               [form.cleaned_data['type'],form.cleaned_data['credits'],form.cleaned_data['name'], form.cleaned_data['score'], form.cleaned_data['level'], form.cleaned_data['adnum'], form.cleaned_data['image'], pk])
            return redirect('certi')
    else:
        form = certiform(initial={'type': item[1],'credits': item[2],'level': item[3], 'adnum': item[4],'name': item[5],'image': item[6], 'score': item[7]})

    context = {
        'form': form,
    }
    return render(request, 'certiupdate.html', context)



@login_required(login_url= '/login/')
def display(request):
    return render(request,'display.html')



@login_required(login_url= '/login/')
def index(request):
    return render(request,'index.html')



@login_required(login_url= '/login/')
def profile(request):
    try:
        contact = Contact.objects.get(staff=request.user)
    except Contact.DoesNotExist:
        contact = None

    return render(request, 'profile.html', {'contact': contact})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render