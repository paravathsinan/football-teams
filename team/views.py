from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Team, User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data['password'])
           user.save()
           login(request, user)
           messages.success(request, 'Registered Successfully!')
           return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html',{'form':form})
    
    
def login_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid email or password!')
    return render(request, 'accounts/login.html')
    
    
def logout_views(request):
    logout(request)
    return redirect('home')

            


def home(request):
    return render(request, 'team/home.html')

@login_required
def explore(request):
    teams = Team.objects.all().order_by('-id')
    
    return render(request, 'team/explore.html', {'teams': teams})

