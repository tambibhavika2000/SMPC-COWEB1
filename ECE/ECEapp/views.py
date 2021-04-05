from django.shortcuts import render,redirect,HttpResponse
from .models import *
import requests
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def noticestudent(request):
    notices=reversed(Notice.objects.all())
    context={
        'notices': notices,
    }
    return render(request,'noticestudent.html',context)


def noticeteacher(request):
    if(request.method=='POST'):
        code = request.POST.get('psw')
        if(code=='1234'):
            notices=reversed(Notice.objects.all())
            context={'notices': notices,}
            return render(request,'noticeteacher.html',context)
        else:
            return render(request,'verify.html')
    return render(request,'verify.html')


def noticeupload(request):
    if(request.method=='POST'):
        title=request.POST.get('title')
        notice=request.FILES['file']
        code = request.POST.get('psw')
        if(code=='1234'):
            notice1=Notice.objects.create(title=title,url=notice)
            notice1.save()
            url = "https://www.fast2sms.com/dev/bulkV2"
            payload = "sender_id=TXTIND&message=New Notice Posted on Notice Board of SVNIT&route=v3&numbers=6350454263"
            headers = {
                'authorization': "HtRglksoXVeP5Jzvjbxa91r6OQpDYcWfAS8T3EBynU2iZhFLdwTSngdN8UGxfKsL7QljX9vbakrHRZhu",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                        }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response)
    return redirect('/student')
            

def delete(request,pk):
    Notice.objects.filter(id=pk).delete()
    return redirect('/teacher')


def research(request):
    P1=reversed(Project.objects.all())
    context={
        'projects':P1
    }
    return render(request,'research.html',context)
        

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('research')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # form2 = AccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registered successfully')
            return redirect('login')

    context = {'form': form,
               }

    return render(request, 'register.html', context)



@login_required(login_url='login')
def update(request):
    if request.method=='POST' and request.user.username!='admin':
        user=request.user
        title=request.POST.get('title')
        abstract=request.POST.get('abstract')
        url=request.POST.get('url')
        type1=request.POST.get('type')
        try:
            project1=Project.objects.create(user=user,title=title,abstract=abstract,url=url, projecttype=type1)
            project1.save()
            A1=Account.objects.get(user=user)
            A1.projects.add(project1)
            A1.save()
            return redirect('profile')
        except:
            return redirect('login')

    elif request.user.username=='admin':
        return redirect('login')
    else:
        return render(request,'update.html')


@login_required(login_url='login')
def profile(request):
    user=request.user
    P1=reversed(Project.objects.filter(user=user))
    context={
        'details':P1
    }
    return render(request,'profile.html',context)


@login_required(login_url='login')
def see(request,pk):
    P1=Project.objects.get(id=pk)
    P2=reversed(Project.objects.filter(user=P1.user))
    context={
        'details':P2,
        'user':P1.user
    }
    return render(request,'profile.html',context)