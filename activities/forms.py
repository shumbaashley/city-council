from django import forms
from django.forms import ModelForm, Textarea
from .models import WeeklyPerfomanceReview, PerfomanceReview
from django.utils.translation import ugettext_lazy as _

class WeeklyPerfomanceReviewForm(ModelForm):
    # activity2 = forms.CharField(required=False)
    # activity3 = forms.CharField(required=False)
    # activity4 = forms.CharField(required=False)
    # activity5 = forms.CharField(required=False)
    # activity6 = forms.CharField(required=False)
    # activity7 = forms.CharField(required=False)

    # work_to_be_done2 = forms.CharField(required=False)
    # work_to_be_done3 = forms.CharField(required=False)
    # work_to_be_done4 = forms.CharField(required=False)
    # work_to_be_done5 = forms.CharField(required=False)
    # work_to_be_done6 = forms.CharField(required=False)
    # work_to_be_done7 = forms.CharField(required=False)

    # work_done1  = forms.CharField(required=False)
    # work_done2  = forms.CharField(required=False)
    # work_done3  = forms.CharField(required=False)
    # work_done4  = forms.CharField(required=False)
    # work_done5  = forms.CharField(required=False)

    # evidence_of_work_done1 = forms.CharField(required=False)
    # evidence_of_work_done2 = forms.CharField(required=False)
    # evidence_of_work_done3 = forms.CharField(required=False)
    # evidence_of_work_done4 = forms.CharField(required=False)
    # evidence_of_work_done5 = forms.CharField(required=False)
    class Meta:
        model = WeeklyPerfomanceReview
        fields = ['employee', 'evaluation', 'innovations', 'activity1', 'activity2', 'activity3', 'activity4', 'activity5', 'activity6', 'activity7', 'work_to_be_done1', 'work_to_be_done2', 'work_to_be_done3', 'work_to_be_done4', 'work_to_be_done5', 'work_to_be_done6', 'work_to_be_done7', 'work_done1', 'week_starting', 'week_ending', 'work_done1', 'work_done2', 'work_done3', 'work_done4', 'work_done5', 'evidence_of_work_done1' , 'evidence_of_work_done2' , 'evidence_of_work_done3' , 'evidence_of_work_done4' , 'evidence_of_work_done5' ]
        labels = {
            "activity1": _("Activity"),
            "activity2": _("Activity"),
            "activity3": _("Activity"),
            "activity4": _("Activity"),
            "activity5": _("Activity"),
            "activity6": _("Activity"),
            "activity7": _("Activity"),
            "work_to_be_done1": _("Work to be done"),
            "work_to_be_done2": _("Work to be done"),
            "work_to_be_done3": _("Work to be done"),
            "work_to_be_done4": _("Work to be done"),
            "work_to_be_done5": _("Work to be done"),
            "work_to_be_done6": _("Work to be done"),
            "work_to_be_done7": _("Work to be done"),
            "work_done1": _("Work Done (Day 1)"),
            "work_done2": _("Work Done (Day 2)"),
            "work_done3": _("Work Done (Day 3)"),
            "work_done4": _("Work Done (Day 4)"),
            "work_done5": _("Work Done (Day 5)"),
            "evidence_of_work_done1": _("Evidence of work done"),
            "evidence_of_work_done2": _("Evidence of work done"),
            "evidence_of_work_done3": _("Evidence of work done"),
            "evidence_of_work_done4": _("Evidence of work done"),
            "evidence_of_work_done5": _("Evidence of work done"),
            "evaluation": _("Evaluation of work done (RESULTS):"),
            "innovations": _("Innovation and Initiatives for the week"),
            
            
        }
        widgets = {
            'evaluation': Textarea(attrs={'cols': 20, 'rows': 5}),
            'innovations': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
        help_texts = {
            'week_starting': _('Use format DD/MM/YYYY.'),
            'week_ending': _('Use format DD/MM/YYYY.'),
        }

class PerfomanceReviewForm(ModelForm):
    class Meta:
        model = PerfomanceReview
        fields = ['work_performance', 'comment_by_supervisor', 'comment_by_director',  ]
        widgets = {
            'comment_by_supervisor': Textarea(attrs={'cols': 80, 'rows': 20}),
            'comment_by_director': Textarea(attrs={'cols': 20, 'rows': 5}),
        }