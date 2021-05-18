from django import forms
from django.forms import ModelForm, Textarea, RadioSelect
from .models import WeeklyPerfomanceReview, Employee
from django.utils.translation import ugettext_lazy as _


class DateInput(forms.DateTimeInput):
    input_type = 'date'

class WeeklyPerfomanceReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(WeeklyPerfomanceReviewForm, self).__init__(*args, **kwargs)
       self.fields['comment_by_supervisor'].widget.attrs['readonly'] = True
       self.fields['comment_by_assistant_director'].widget.attrs['readonly'] = True
       self.fields['checked_and_approved'].disabled = True
       self.fields['comment_by_director'].widget.attrs['readonly'] = True

       
    class Meta:
        model = WeeklyPerfomanceReview
        exclude = ('employee', 'department')
        labels = {
            "week_starting": _(""),
            "week_ending": _(""),
            "activity1": _("Activity"),
            "activity2": _("Activity"),
            "activity3": _("Activity"),
            "activity4": _("Activity"),
            "activity5": _("Activity"),
            "activity6": _("Activity"),
            "activity7": _("Activity"),
            "work_to_be_done1": _("Work to be Done"),
            "work_to_be_done2": _("Work to be Done"),
            "work_to_be_done3": _("Work to be Done"),
            "work_to_be_done4": _("Work to be Done"),
            "work_to_be_done5": _("Work to be Done"),
            "work_to_be_done6": _("Work to be Done"),
            "work_to_be_done7": _("Work to be Done"),
            "work_done1": _("Work Done (Day 1)"),
            "work_done2": _("Work Done (Day 2)"),
            "work_done3": _("Work Done (Day 3)"),
            "work_done4": _("Work Done (Day 4)"),
            "work_done5": _("Work Done (Day 5)"),
            "evidence_of_work_done1": _("Evidence of Work Done"),
            "evidence_of_work_done2": _("Evidence of Work Done"),
            "evidence_of_work_done3": _("Evidence of Work Done"),
            "evidence_of_work_done4": _("Evidence of Work Done"),
            "evidence_of_work_done5": _("Evidence of Work Done"),
            "evaluation": _("Evaluation of Work Done (RESULTS):"),
            "innovations": _("Innovation and Initiatives for the Week"),
            "comment_by_supervisor": _("Comments by Immediate Supervisor"),
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
            'week_starting': DateInput(),
            'week_ending': DateInput(),
        }


class EmployeeProfileForm(ModelForm):
      
    class Meta:
        model = Employee
        exclude = ('id', 'user', 'department', 'medical_records', 'leave_record', 'displinary_record', 'date_joined', 'salary', 'grade', 'qualifications' , 'sex' )
        labels = {
            "photo": _(""),
            "date_of_birth": _(""),
            "marital_status": _(""),
            "home_address": _(""),
            "phone_number": _(""),
            "next_of_kin_name": _(""),
            "next_of_kin_phone_number": _(""),
        }
        widgets = {
            'home_address': Textarea(attrs={'cols': 20, 'rows': 5}),
            'date_of_birth': DateInput(),
        }


    # photo 
    # date_of_birth
    # sex 
    # marital_status  
    # home_address 
    # phone_number 
    # next_of_kin_name 
    # next_of_kin_phone_number 
    # grade 
    # salary 
    # qualifications 
    # medical_records  
    # leave_record 
    # date_joined 
    