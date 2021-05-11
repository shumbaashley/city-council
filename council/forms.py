from django import forms

class WorkPlanForm(forms.Form):
    activity1 = forms.CharField(max_length=100)
    worktobedone1 = forms.CharField(max_length=100)
    activity2 = forms.CharField(max_length=100)
    worktobedone2 = forms.CharField(max_length=100)
    activity3 = forms.CharField(max_length=100)
    worktobedone3 = forms.CharField(max_length=100)
    activity4 = forms.CharField(max_length=100)
    worktobedone4 = forms.CharField(max_length=100)
    activity5 = forms.CharField(max_length=100)
    worktobedone5 = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    weekstarting = forms.DateField()
    weekending = forms.DateField()