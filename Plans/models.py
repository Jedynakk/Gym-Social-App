from django.db import models
from Accounts.models import Profile
from Exercises.models import Exercise





DAYS = (
    (1, 'MONDAY'),
    (2, 'TUESDAY'),
    (3, 'WEDNESDAY'),
    (4, 'THURSDAY'),
    (5, 'FRIDAY'),
    (6, 'SATURDAY'),
    (7, 'SUNDAY'),

)


def __str__(self):
    return self.name


SI = (
    (1, 'KG'),
    (2, 'LBS'),
    (3, 'KM'),
    (4, 'MI')
)


class Plan(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, null=True)
    like = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.name

class ExerciseToPlan(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    day_name = models.IntegerField(choices=DAYS, default=1)
    

class Set(models.Model):
    exercise_to_plan = models.ForeignKey(ExerciseToPlan, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    si = models.IntegerField(choices=SI, default=1)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)


class CurrentPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)



