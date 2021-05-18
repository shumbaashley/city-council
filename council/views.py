from council.models import Employee, Department
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import WeeklyPerfomanceReviewForm, EmployeeProfileForm
from django.shortcuts import get_object_or_404
from .models import WeeklyPerfomanceReview
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return render(request, "council/login.html", {"message": None})

    employee =  get_object_or_404(Employee, user=request.user)
    table_info = WeeklyPerfomanceReview.objects.filter(employee=employee)[0:10]
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


def profile(request):
    employee =  get_object_or_404(Employee, user=request.user)
    data = {
        "user": request.user,
        "employee": employee
      }
    return render(request, 'council/profile.html', data)


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


def create_performance_review(request):
    form = WeeklyPerfomanceReviewForm()

    if request.method == "POST":
        form = WeeklyPerfomanceReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            employee =  get_object_or_404(Employee, user=request.user)
            department =  get_object_or_404(Department, id=employee.department.id)
            review.employee = employee
            review.department = department
            review.save()
            messages.success(request, 'Your perfomance review has been created.')
            return HttpResponseRedirect(reverse("council:index"))

    return render(request, "council/create_performance_review.html", {
        "form" : form
    })


def edit_performance_review(request, review_id):
    form = WeeklyPerfomanceReviewForm(instance = WeeklyPerfomanceReview.objects.get(id=review_id))

    if request.method == "POST":
        form = WeeklyPerfomanceReviewForm(request.POST, instance = WeeklyPerfomanceReview.objects.get(id=review_id))

        if form.is_valid():
            form.save()
            messages.success(request, 'Your perfomance review has been updated.')
            return HttpResponseRedirect(reverse("council:index"))

    return render(request, "council/edit_performance_review.html", {
        "form" : form
    })

def edit_profile(request, employee_id):
    form = EmployeeProfileForm(instance = Employee.objects.get(id=employee_id))
    employee =  get_object_or_404(Employee, user=request.user)

    if request.method == "POST":
        form = EmployeeProfileForm(request.POST, request.FILES, instance = Employee.objects.get(id=employee_id))
        print("gets here")

        if form.is_valid():
            print("works")
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return HttpResponseRedirect(reverse("council:profile"))

    return render(request, "council/edit_profile.html", {
        "form" : form,
        'employee' : employee
    })
