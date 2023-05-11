from django.urls import path
from MainApp import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('search/', views.Search, name='search'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='my_profile'),
    path('allprofiles/', views.AllProfilesView.as_view(), name='all_profiles'),
    path('sentrequest/<int:id>', views.FriendReqeust, name='request'),
    path('friendsrequest/', views.RequestListView.as_view(), name='requests_list'),
    path('accept_request/<int:id>', views.Accept, name='accept_request'),
    path('friends_list/', views.FriendsListView.as_view(), name='friends_list'),
    path('delete_friend/<int:id>', views.DeleteFriend, name='delete_friend'),
    path('delete_post/<int:id>', views.DeletePost, name='delete_post'),
    path('like_post/<int:id>', views.Like, name='like_post'),
    path('delete_request/<int:id>', views.DeleteRequest, name='delete_request'),
    path('update_profile/<int:pk>', views.UpdateProfileView.as_view(), name='update_profile'),
    path('today', views.TodayView.as_view(), name='today')
]
