from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import Code
# Create your views here.

def index(request):
    return render(request, 'account/signup.html', {'message':'Sign Up using this form.'})


def signup(request):
    code = Code.objects.get(id=1)
    liste = []
    X = User.objects.all()
    for i in X:
        u = i.username
        print(u)
        liste.append(u)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        post = request.POST
        for i in post.values():
            print(i)
            if i == '':
                return render(request, 'account/signup.html', {'message':'Your form input is empty !'})

        if str(password2) == str(code):
            if username in liste:
                return render(request, 'account/signup.html', {'message':'Username is already taken !'})
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    password = password
                )
                user.save()
                profile = Profile.objects.create(user=user)
                profile.save()
                return render(request, 'account/to_login.html',  {'user':user})
        else:
            return render(request, 'account/signup.html', {'message':'Junior password is wrong !'})
    else:
        return render(request, 'account/signup.html', {'message':'Something is wrong !'})
