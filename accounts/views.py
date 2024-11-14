from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import WebUserRegistrationForm, PanelAdminRegistrationForm, CustomLoginForm
from .models import WebUser, PanelAdmin

def register_webuser(request):
    if request.method == "POST":
        form = WebUserRegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Form errors:", form.errors)  # Print form errors to debug
    else:
        form = WebUserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

def register_paneladmin(request):
    if request.method == "POST":
        form = PanelAdminRegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect("login")
    else:
        form = PanelAdminRegistrationForm()
        print("else")
    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        print(request.POST)
        # print()
        print(form.is_valid())
        # if form.is_valid():
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(email)
        user = authenticate(request, username=email, password=password)
        if user is not None:
                login(request, user)
                # return redirect('dashboard')
                return HttpResponse("jnddjn")
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('login')
