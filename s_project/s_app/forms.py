from django import forms
from django.core import validators
from s_app.models import User

#
def check_for_t(value):
    if value[0].lower!='t':
        raise forms.ValidationError("Please enter a name which starts with letter t")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_t])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required = False,widget = forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
