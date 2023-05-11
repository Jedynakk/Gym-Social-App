from django import forms
from Exercises.models import Exercise, MUSCLE
from Plans.models import ExerciseToPlan



class AddExercieseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle', 'exercise_image']

        widget = {
            'name':forms.TextInput(),
            'description':forms.TextInput(),
            'muscle':forms.Select()
        }


class AddExerciseToPlanForm(forms.ModelForm):
    class Meta:
        model = ExerciseToPlan
        fields = ['plan', 'day_name']
        