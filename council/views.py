from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import WorkPlanForm

@login_required
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


@login_required
def logout_view(request):
    logout(request)
    return render(request, "council/login.html", {"message": "Logged out."})
    
@login_required
def activities(request):
    data = {}
    return render(request, 'council/activities.html', data)

@login_required
def profile(request):
    data = {
        "user": request.user
      }
    return render(request, 'council/profile.html', data)

@login_required
def performance(request):
    data = {
        "user": request.user
      }
    return render(request, 'council/performance.html', data)

@login_required
def dashboard(request):
    data = {}
    return render(request, 'council/dashboard.html', data)

@login_required
def work_plans(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        activity1 = request.POST["activity1"]
        worktobedone1 = request.POST["worktobedone1"]
        activity2 = request.POST["activity2"]
        worktobedone2 = request.POST["worktobedone2"]
        activity3 = request.POST["activity3"]
        worktobedone3 = request.POST["worktobedone3"]
        activity4 = request.POST["activity4"]
        worktobedone4 = request.POST["worktobedone4"]
        activity5 = request.POST["activity5"]
        worktobedone5 = request.POST["worktobedone5"]
        weekstarting = request.POST["weekstarting"]
        weekending = request.POST["weekending"]
        
        return HttpResponseRedirect(reverse("council:work-plans"))

    else:

        return render(request, 'council/workplans.html', {})