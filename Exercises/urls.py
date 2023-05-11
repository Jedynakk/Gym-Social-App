from django.urls import path
from Exercises import views


urlpatterns = [
    path('add_exercise/', views.AddExercieView.as_view(), name='add_exercise'),
    path('exercises_list/', views.ExercisesListView.as_view(), name='exercises_list'),
    path('exercise/<int:id>/', views.ExerciseView.as_view(), name='exercise'),
]