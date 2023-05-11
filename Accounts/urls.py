from django.urls import path
from Accounts import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('create_account/', views.NewUserView.as_view(), name="new_user"),
]