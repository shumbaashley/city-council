from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from activities.forms import WeeklyPerfomanceReviewForm
from .forms import WorkPlanForm

def index(request):
    if not request.user.is_authenticated:
        return render(request, "council/login.html", {"message": None})
    context = {
          "user": request.user
      }
    return render(request, 'council/dashboard.html', context)


def login_view(request):
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return HttpResponseRedirect(reverse("council:index"))
      else:
          return render(request, "council/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "council/login.html", {"message": "Logged out."})
    
def activities(request):
    data = {}
    return render(request, 'council/activities.html', data)

def profile(request):
    data = {
        "user": request.user
      }
    return render(request, 'council/profile.html', data)

def performance(request):
    data = {
        "user": request.user
      }
    return render(request, 'council/performance.html', data)

def dashboard(request):
    data = {}
    return render(request, 'council/dashboard.html', data)

def work_plans(request):
    if request.method == "POST":  
        form = WeeklyPerfomanceReviewForm(request.POST)  
        if form.is_valid():  
            try:  
                return HttpResponseRedirect(reverse("council:index"))
            except:  
                return HttpResponse("Error")  
 
    else:
        form = WeeklyPerfomanceReviewForm()
        return render(request, 'council/workplans.html', {'form' : form})



