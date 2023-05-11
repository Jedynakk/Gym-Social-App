from django.db import models


MUSCLE = (
    (0, 'DEFAULT'),
    (1, 'ABS'),
    (2, 'BACK'),
    (3, 'BISEPSC'),
    (4, 'CARDIO'),
    (5, 'CHEST'),
    (6, 'GLUTES'),
    (7, 'LEGS'),
    (8, 'SHOULDERS'),
    (9, 'TRICPES'),

)

class Exercise(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(null=False)
    muscle = models.IntegerField(choices=MUSCLE, default=0)
    exercise_image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

