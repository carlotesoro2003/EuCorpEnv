from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth



class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email is already used'}, status=409)
        return JsonResponse({'email_valid': 'true'})



class LoginView(View):
    def get(self, request):
        # Render the login page
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # Authenticate user
            user = auth.authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)  

                if user.is_superuser:
                    return redirect('dashboard')  
                else:
                    return redirect('dashboard')  
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill all fields.')
        return render(request, 'authentication/login.html')




class LogoutView(View):
    def post(self, request):
        # Clear session data and invalidate the session
        request.session.flush()
        
        # Optional: Add a success message
        messages.success(request, 'You have been logged out successfully.')
        
        # Redirect to the login page
        return redirect('login')  # Make sure 'login' is correctly defined in urls.py
