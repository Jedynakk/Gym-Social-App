from django import forms
from Accounts.models import User
from django.core.exceptions import ValidationError

class NewUserForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form', 'placeholder': 'PASSWORD'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'REPEAT PASSWORD', 'class':'form'}),label='')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form', 'placeholder':'USERNAME'}),
            'first_name':forms.TextInput(attrs={'class':'form', 'placeholder':'NAME'}),
            'last_name':forms.TextInput(attrs={'class':'form', 'placeholder':'SURNAME'}),
        }
        labels = {
            'username':"",
            'first_name':"",
            'last_name':""

        }

        help_texts = {
            'username': None,
            'email': None,
        }
        
    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Hasła się nie zgadzają!')
        return data
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'LOGIN', 'class':'form'}), label="")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD','class':'form'}), label="")
