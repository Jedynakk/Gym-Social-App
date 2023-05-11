from django.shortcuts import render, redirect
from django.views import View
from Plans.models import Plan, ExerciseToPlan, DAYS, Set,  CurrentPlan
from Accounts.models import Profile
from Plans.forms import AddPlanForm, AddSetForm
from datetime import date
from django.db.models import Q


class AddPlanView(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        form = AddPlanForm()
        return render(request, 'plan/add_plan.html', {'form':form, 'profile':profile})

    def post(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        form = AddPlanForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author_id = current_user.pk
            f.date = date.today()
            f.save()
            return redirect ('home')
        return render(request, 'plan/add_plan.html', {'form':form, 'profile':profile})
    
class AllPlansList(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        plans = Plan.objects.all()
        searched = request.GET.get('searched', default='')
        if searched != "":
            plans = plans.filter(name__icontains=searched)
        return render(request, 'plan/all_plans.html', {'plans':plans, 'profile':profile})

class PlanView(View):
    def get(self, request, id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        plan = Plan.objects.get(pk=id)
        exercise_to_plan = ExerciseToPlan.objects.filter(plan_id=plan.pk).order_by('day_name')
        days = DAYS
        return render(request, 'plan/plan_details.html', {'plan':plan, 'profile':profile, 'exercise_to_plan':exercise_to_plan, 'days':days})


class ExerciseInPlanView(View):
    def get(self, request, id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        exercise_to_plan = ExerciseToPlan.objects.get(pk=id)
        sets = Set.objects.filter(exercise_to_plan_id=exercise_to_plan.pk).filter(author_id=current_user.pk)
        form = AddSetForm()
        return render(request, 'exercise_in_plan/exercise_in_plan.html', {'profile':profile, 'exercise_to_plan':exercise_to_plan, 'form':form, 'sets':sets})
    


    def post(self, request, id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        exercise_to_plan = ExerciseToPlan.objects.get(pk=id)
        form = AddSetForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author_id = current_user.pk
            f.date = date.today()
            f.exercise_to_plan_id = exercise_to_plan.pk
            f.save()     
            form = AddSetForm()
        return render(request, 'exercise_in_plan/exercise_in_plan.html', {'profile':profile, 'exercise_to_plan':exercise_to_plan, 'form':form})




def SetPlanAsCurrent(request, id):
    plan = Plan.objects.get(pk=id)
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    if CurrentPlan.objects.filter(current_user_id=current_user.pk).count() != 0:
        CurrentPlan.objects.filter(current_user_id=current_user.pk).delete()
        CurrentPlan.objects.create(current_user_id=current_user.pk, plan_id=plan.pk)
    else:
        CurrentPlan.objects.create(current_user_id=current_user.pk, plan_id=plan.pk)
    return redirect ('all_plans')