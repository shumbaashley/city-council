from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import WeeklyPerfomanceReviewForm, PerfomanceReviewForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WeeklyPerfomanceReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')


    else:
        form = WeeklyPerfomanceReviewForm()
        form3 = PerfomanceReviewForm()

    return render(request, 'activities/name.html', {
        'form': form,
        'form3': form3,
        })


def edit(request, id=None, template_name='edit_review.html'):
    # if id:
    #     article = get_object_or_404(WorkPlan, pk=id)
    #     if article.author != request.user:
    #         return HttpResponseForbidden()
    # else:
    #     article = Article(author=request.user)

    # form = WorkPlan(request.POST or None, instance=article)
    # if request.POST and form.is_valid():
    #     form.save()

    #     # Save was successful, so redirect to another page
    #     redirect_url = reverse(article_save_success)
    #     return redirect(redirect_url)

    return render(request, template_name, {
        # 'form': form
    })