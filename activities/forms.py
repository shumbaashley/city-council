from django import forms
from django.forms import ModelForm
from .models import Author

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.DateField()
    cc_myself = forms.BooleanField(required=False)




class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']