from django import forms
from django.forms import ModelForm
from .models import WorkPerformance, WorkPlan, PerfomanceReview

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.DateField()
    cc_myself = forms.BooleanField(required=False)



class WorkPerformanceForm(ModelForm):
    class Meta:
        model = WorkPerformance
        fields = ['supervisor', 'work_plan', 'work_done', 'evidence_of_work_done']



class WorkPlanForm(ModelForm):
    class Meta:
        model = WorkPlan
        fields = ['employee', 'activities', 'work_to_be_done', 'week_starting', 'week_ending']


class PerfomanceReviewForm(ModelForm):
    class Meta:
        model = PerfomanceReview
        fields = ['work_performance', 'comment_by_supervisor', 'comment_by_director',  ]
        
