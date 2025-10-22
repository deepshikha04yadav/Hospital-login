from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    form = SignupForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    return render(request, 'login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
