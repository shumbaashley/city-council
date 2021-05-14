from council.models import Employee
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from activities.forms import WeeklyPerfomanceReviewForm
from django.shortcuts import get_object_or_404
from activities.models import WeeklyPerfomanceReview
from django.shortcuts import redirect


def index(request):
    if not request.user.is_authenticated:
        return render(request, "council/login.html", {"message": None})

    employee =  get_object_or_404(Employee, user=request.user)
    table_info = WeeklyPerfomanceReview.objects.filter(employee=employee)
    data = {
        "user": request.user,
        "table_info" : table_info
      }
    return render(request, 'council/dashboard.html', data)


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
    employee =  get_object_or_404(Employee, user=request.user)
    data = {
        "user": request.user,
        "employee": employee
      }
    return render(request, 'council/profile.html', data)

def performance(request):
    employee =  get_object_or_404(Employee, user=request.user)
    table_info = WeeklyPerfomanceReview.objects.filter(employee=employee)
    data = {
        "user": request.user,
        "table_info" : table_info
      }
    return render(request, 'council/basic_table.html', data)

def dashboard(request):
    data = {}
    return render(request, 'council/dashboard.html', data)

def work_plans(request):
    if request.method == "POST":  
        form = WeeklyPerfomanceReviewForm(request.POST)  
        
        if form.is_valid():
            new_review = form.save()
            # employee =  get_object_or_404(Employee, pk=request.user.id)
            # new_review.employee = employee
            # new_review.save()  
            return HttpResponseRedirect(reverse("council:index"))  
    else:
        form = WeeklyPerfomanceReviewForm()
        return render(request, 'council/workplans.html', {'form' : form})



def edit(request, id=None, template_name='council/edit_review.html'):
    instance = get_object_or_404(WeeklyPerfomanceReview, pk=id)
    if request.method == "POST":
        form = WeeklyPerfomanceReviewForm(request.POST, instance=instance)
        # if form.is_valid():
        #     form.save()
    else:
        form = WeeklyPerfomanceReviewForm(instance=instance)

    return render(request, template_name, {
        'form': form,
        'id': id,
    })


def review_edit(request, id):
    # review = get_object_or_404(WeeklyPerfomanceReview, pk=pk)
    # if request.method == "POST":
    #     form = WeeklyPerfomanceReviewForm(request.POST, instance=review)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.save()
    #         render(request, 'council/edit_review.html', {'form': form, 'id' : pk})
    # else:
    #     form = WeeklyPerfomanceReviewForm(instance=review)
    # return render(request, 'council/edit_review.html', {'form': form, 'id' : pk})

  # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(WeeklyPerfomanceReview, id = id)
  
    # pass the object as instance in form
    form = WeeklyPerfomanceReviewForm(request.POST or None, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
  
    # add form dictionary to context
    context["form"] = form
    context["id"] = id
  
    return render(request, "council/edit_review.html", context)



# delete view for details
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(WeeklyPerfomanceReview, id = id)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
  
    return render(request, "delete_view.html", context)