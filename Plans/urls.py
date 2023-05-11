from django.urls import path
from Plans import views

urlpatterns = [
    path('add_plan/', views.AddPlanView.as_view(), name='add_plan'),
    path('plan_list/', views.AllPlansList.as_view(), name='all_plans'),
    path('plan_details/<int:id>', views.PlanView.as_view(), name='plan_details'),
    path('exercise_in_plan/<int:id>', views.ExerciseInPlanView.as_view(), name='exercise_in_plan'),
    path('setcurrentplan/<int:id>', views.SetPlanAsCurrent, name='set_current_plan')
]