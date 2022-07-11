from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('polls:index'))
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error"))
            return redirect('login_u')
    return render(request, 'registration/login.html', {})   