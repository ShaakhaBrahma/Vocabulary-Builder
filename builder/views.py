from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import functions
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
@login_required()
def signup(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        query = User.objects.all()
        print(query)
        if User.objects.filter(username=username).exists():
            print(query)
            messages.error(request, 'username exist!')
            return redirect('builder:home')

        else:
            user = User.objects.create_user(first_name=name, username= username, password= raw_password)
            user.profile.filename = name+'.txt'
            user.profile.save()
            user.save()
            login(request, user)
            return redirect('builder:search', request.user)


def signin(request):

    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'POST':

        username = request.POST.get('username1')
        password = request.POST.get('password1')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('builder:search', request.user)
        else:
            messages.error(request, 'username or password not correct')
            return redirect('builder:home')
def search(request, username):
    if request.method == 'GET':
        return render(request, 'search.html', context={'username': username})
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword:
            if request.POST.get('add')=="add":
                print("add button")
                meaning = functions.searchInIndex(keyword.capitalize())
                if meaning!="Word is not in file":
                    user = User.objects.get(username=username)
                    filename=user.profile.filename
                    f = open(filename,'a')
                    f.write(keyword+'\n')
                    f.close()
                redirect('builder:search',request.user)
            meaning = functions.searchInIndex(keyword.capitalize())
            return render(request, 'search.html', context={'meaning': meaning, 'username':username})
        else:
            return render(request, 'search.html', context={'username': username})


def showlist(request):
    if request.method == 'GET':
        username=request.user
        user = User.objects.get(username=username)
        filename = user.profile.filename
        f=open(filename,'r')
        list=[]
        for word in f:
            list.append(word)
        list.sort()
        return render(request, 'search.html', context={'username': username, 'mylist':list})
    if request.method == 'POST':
        redirect('builder:search',request.user)
