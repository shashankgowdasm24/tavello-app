from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['psw']
        password_repeat = request.POST['psw-repeat']
        email = request.POST['email']

        if password == password_repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User Created')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/accounts/login')
    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credential")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')