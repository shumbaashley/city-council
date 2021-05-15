from django import forms
from django.forms import ModelForm, Textarea, RadioSelect
from .models import WeeklyPerfomanceReview
from django.utils.translation import ugettext_lazy as _

class WeeklyPerfomanceReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(WeeklyPerfomanceReviewForm, self).__init__(*args, **kwargs)
       self.fields['comment_by_supervisor'].widget.attrs['readonly'] = True
       self.fields['comment_by_assistant_director'].widget.attrs['readonly'] = True
       self.fields['checked_and_approved'].disabled = True
       self.fields['comment_by_director'].widget.attrs['readonly'] = True

       
    class Meta:
        model = WeeklyPerfomanceReview
        exclude = ('employee',)
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
            "comment_by_supervisor": _("Comments by immediate Supervisor"),
            "comment_by_assistant_director": _("Comments by Assistant Director of Finance"),
            "comment_by_director": _("Comments by Director of Finance"),
            "checked_and_approved": _("Checked and Approved as a true record"),
        }
        widgets = {
            'evaluation': Textarea(attrs={'cols': 20, 'rows': 5}),
            'innovations': Textarea(attrs={'cols': 20, 'rows': 5}),
            'comment_by_supervisor': Textarea(attrs={'cols': 20, 'rows': 5}),
            'comment_by_assistant_director': Textarea(attrs={'cols': 20, 'rows': 5}),
            'comment_by_director': Textarea(attrs={'cols': 20, 'rows': 5}),
               }
        help_texts = {
            'week_starting': _('Use format YYYY-MM-DD.'),
            'week_ending': _('Use format YYYY-MM-DD.'),
        }