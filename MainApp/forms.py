from django import forms
from Accounts.models import Post, Profile
from django.forms.widgets import FileInput


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'post_image']
        widgets = {
            'text':forms.TextInput(attrs={'class':'form', 'placeholder':'POST'}),
            'post_image':FileInput()
        }
        labels = {
            'text':"",
            'post_image':"",
        }



class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'height', 'weight']



