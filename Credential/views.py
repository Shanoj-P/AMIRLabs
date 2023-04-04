from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        username = request.POST['Username']

        email = request.POST['email']
        password = request.POST['password']
        cPassword = request.POST['Cpassword']

        if password == cPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('/register/')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password,)
                user.save()
                return redirect('/login/')
        else:
            messages.info(request, "Password does not match")
            return redirect('/register/')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('feedsApp:home')
        else:
            messages.info(request, 'User credentials does not match')
            return redirect('/login/')


def logout(request):
    auth.logout(request)
    return redirect('/')
