from django.contrib.auth import authenticate, login  # Import authenticate and login functions
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        age = request.POST.get('Age')
        date_of_birth = request.POST.get('Date of Birth')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Create user with email as username
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, "User registered successfully")
            return redirect('login')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('register')

    return render(request, 'register.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')  # Assuming you have a view named 'user_dashboard'
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')

