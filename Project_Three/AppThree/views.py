from django.shortcuts import render
from AppThree.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    context_dict = {"text":"Hello world", "number":100}
    return render(request,"AppThree/index.html",context_dict)

def other(request):
    return render(request,"AppThree/other.html")

def relative(request):
    return render(request,"AppThree/relative.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def logged_in(request):
    return HttpResponse("You're logged in")
    
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)        
            profile.user = user
            
            if "profile_picture" in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
                
            profile.save()
                
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,"AppThree/registration.html",
                  {
                      "user_form":user_form,
                      "profile_form":profile_form,
                      "registered":registered
                    })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            
            else:
                return HttpResponse("Accound Not Active")
            
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login details")
    else:
        return render(request,"AppThree/login.html",{})