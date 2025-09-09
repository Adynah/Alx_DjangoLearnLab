from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # log user in after registering
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "registration/profile.html")

def home_view(request):
    return render(request, "home.html")

class StaticLoginView(TemplateView):
    template_name = 'blog/static/login.html'

class StaticRegisterView(TemplateView):
    template_name = 'blog/static/register.html'

