from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import WorkPerformanceForm, WorkPlanForm, PerfomanceReviewForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkPerformanceForm(request.POST)


        # form2 = WorkPerformanceForm(request.POST)
        # form3 = PerfomanceReviewForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # sender = form.cleaned_data['sender']
            # cc_myself = form.cleaned_data['cc_myself']

            # recipients = ['info@example.com']
            # if cc_myself:
                # recipients.append(sender)

            # send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')



            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkPlanForm()
        form2 = WorkPerformanceForm()
        form3 = PerfomanceReviewForm()

    return render(request, 'activities/name.html', {
        'form': form,
        'form2': form2,
        'form3': form3,
        })