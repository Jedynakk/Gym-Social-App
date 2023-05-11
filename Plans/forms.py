from django import forms
from Plans.models import Plan, Set

class AddPlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description']


        widgets = {
            'name':forms.TextInput(attrs={'class':'form', 'placeholder':'NAME OF PLAN'}),
            'description':forms.Textarea(attrs={'class':'form_descrioption', 'placeholder':'DESCRIPTION'})
        }

        labels = {
            'name':'',
            'description':''
        }


class AddSetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['reps', 'weight', 'si',]