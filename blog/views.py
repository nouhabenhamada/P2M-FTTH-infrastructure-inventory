from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "blog/login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password') 
        new_user = User.objects.create_user(username=name, email= email, password=password)
        new_user.save()
        return redirect('/login')
    return render(request, "blog/signup.html")

def login_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request, "blog/login.html")


@login_required
def home(request):
    if request.user is None :
        
        return redirect('/login')

    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(request, "blog/home.html", context)

@login_required
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        coordinates = request.POST.get('coordinates')  
        latitude, longitude = map(float, coordinates.split(', '))  
        remarks = request.POST.get('remarks')
        new_post = Posts(title=title, content=content, author=request.user, latitude=latitude, longitude=longitude, remarks=remarks)
        new_post.save()
        return redirect("/home")
    else:
        return render(request, 'blog/new_post.html')  


@login_required
def mypost(request):
    posts = Posts.objects.filter(author=request.user)
    print(posts)

    context = {
        'posts': posts
        }
    return render(request, 'blog/my_post.html',context)

def sign_out(request):
    logout(request)
    return redirect('/login')

def map_page(request):
    return render(request, 'blog/index.html')



