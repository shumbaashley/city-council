from django import forms
from django.forms import ModelForm
from .models import WorkPlan, PerfomanceReview

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.DateField()
    cc_myself = forms.BooleanField(required=False)

class WorkPlanForm(ModelForm):
    class Meta:
        model = WorkPlan
        fields = ['employee', 'activities', 'work_to_be_done', 'week_starting', 'week_ending', 'supervisor', 'work_done', 'evidence_of_work_done']


class PerfomanceReviewForm(ModelForm):
    class Meta:
        model = PerfomanceReview
        fields = ['work_performance', 'comment_by_supervisor', 'comment_by_director',  ]
        
class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )