from django.shortcuts import render, redirect
from django.views import View
from Exercises.forms import AddExercieseForm
from Exercises.models import Exercise, MUSCLE
from Accounts.models import Profile
from Exercises.forms import AddExerciseToPlanForm


class AddExercieView(View):
    def get(self, request):
        form = AddExercieseForm()
        return render(request, 'exercise/add_exercise.html', {'form':form})
    
    def post(self, request):
        form = AddExercieseForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_exercises")
        return render(request, 'exercise/add_exercise.html', {'form':form})


class ExercisesListView(View):
    def get(self,request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        exercises = Exercise.objects.all()
        searched = request.GET.get('searched', default='')
        muscle = request.GET.get('muscle', '0')

        if muscle != '0':
            exercises = exercises.filter(muscle=muscle)
        if searched != "":
            exercises = exercises.filter(name__icontains=searched)
        return render(request, 'exercise/exercise_list.html', {'exercises':exercises, 'muscle':MUSCLE, 'profile':profile, })
  


class ExerciseView(View):
    def get(self, request,id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        exercise = Exercise.objects.get(pk=id)
        form = AddExerciseToPlanForm()
        return render(request, 'exercise/exercise.html', {'exercise':exercise, 'profile':profile, 'form':form})
    
    def post(self, request, id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        exercise = Exercise.objects.get(pk=id)
        form = AddExerciseToPlanForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.exercise = exercise
            f.save()
            return redirect('exercise', exercise.pk)
        return render(request, 'exercise/exercise.html', {'exercise':exercise, 'profile':profile, 'form':form})