from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return render(request, "council/login.html", {"message": None})
    context = {
          "user": request.user
      }
    return render(request, 'council/index.html', context)

def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': 'question'})

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