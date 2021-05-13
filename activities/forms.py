from django import forms
from django.forms import ModelForm, Textarea
from .models import WorkPlan, PerfomanceReview
from django.utils.translation import ugettext_lazy as _

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.DateField()
    cc_myself = forms.BooleanField(required=False)

class WorkPlanForm(ModelForm):
    class Meta:
        model = WorkPlan
        fields = ['employee', 'activities', 'work_to_be_done', 'week_starting', 'week_ending', 'supervisor', 'work_done', 'evidence_of_work_done']
        labels = {
            "week_starting": _("Activity"),
            "week_ending": _("Activity"),
        }

class PerfomanceReviewForm(ModelForm):
    class Meta:
        model = PerfomanceReview
        fields = ['work_performance', 'comment_by_supervisor', 'comment_by_director',  ]
        widgets = {
            'comment_by_supervisor': Textarea(attrs={'cols': 80, 'rows': 20}),
            'comment_by_director': Textarea(attrs={'cols': 20, 'rows': 5}),
        }