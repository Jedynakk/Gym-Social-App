from django.shortcuts import render, redirect
from django.views import View
from Accounts.models import User, Profile, RequestFriends, Friends, Post, LikePost
from datetime import date
from MainApp.forms import AddPostForm, UpdateProfileForm
from Plans.models import CurrentPlan, DAYS,ExerciseToPlan
import random
from django.db.models import Q
from django.urls import reverse
from django.views.generic import UpdateView
from datetime import datetime



class HomeView(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        posts = Post.objects.all()
        form = AddPostForm() 
        liked_posts = []
    
        return render(request, 'home.html', {'current_user':current_user,'profile':profile, 'form':form, 'posts':posts, 'liked_posts':liked_posts})

    def post(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        posts = Post.objects.all()
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.author_id = current_user.pk
            f.date = date.today()
            f.save()
            form = AddPostForm()
        return render(request, 'home.html', {'current_user':current_user,'profile':profile, 'form':form, 'posts':posts})
 



def DeletePost(request, id):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')


def Like(request, id):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    post = Post.objects.get(pk=id)
    liked = LikePost.objects.filter(current_user_id=current_user.pk).filter(post_id=post.id).count()
    if liked == 0:
        LikePost.objects.create(current_user_id=profile.pk, post_id=post.pk)
    else:
        LikePost.objects.get(current_user_id=profile.pk, post_id=post.pk).delete()
    return redirect('home')

def Search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        searched_user = User.objects.filter(username__contains=searched)
        return render(request, 'other/search.html', {'searched':searched, 'searched_user':searched_user,'profile':profile})
    else:
        return render(request, 'other/search.html', {'searched':searched,  'searched_user':searched_user,'profile':profile})
    
    

class ProfileView(View):
    def get(self, request, id):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        friends = Friends.objects.filter(Q(current_user_id=current_user.pk) | Q(friend_id=current_user.pk)).count()
        form = AddPostForm()
        return render(request, 'profile.html'
        , {'profile':profile, 'current_user':current_user, 'form':form, 'friends':friends})
    

class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'update_profile.html'
    fields = ['profile_image', 'height', 'weight', 'bio']

    def get_success_url(self):
        return reverse("home")

class AllProfilesView(View):
    def get(self, request):
        current_user = request.user
        all_profiles = Profile.objects.exclude(user_id=current_user.pk)
        profile = Profile.objects.get(user_id=current_user.pk)
        return render(request, 'friendship/profiles.html', {"all_profiles":all_profiles,'profile':profile,})
    
  

def FriendReqeust(request, id):
    current_user = request.user
    profile = Profile.objects.get(pk=id)
    sent = date.today()

    request_counter = RequestFriends.objects.filter(sender_id=current_user.pk, recipient_id=profile.pk).count()
    if request_counter == 0:
        RequestFriends.objects.create(sender_id=current_user.pk, recipient_id=profile.pk, sent=sent)
    else:
        pass
    return redirect("all_profiles")

def DeleteRequest(request, id):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    friend_request = RequestFriends.objects.get(pk=id)
    friend_request.delete()
    return redirect('requests_list')



class RequestListView(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        friend_requests = RequestFriends.objects.filter(recipient_id=profile.pk)
        fri_req = RequestFriends.objects.filter(sender_id=profile.pk)
        return render(request, 'friendship/friend_request_list.html',
                       {'profile':profile, 'friend_requests':friend_requests, 'fri_req':fri_req})

    

def Accept(request , id):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    friend_request = RequestFriends.objects.get(pk=id)
    Friends.objects.create(friend_id = friend_request.sender.pk, current_user_id = friend_request.recipient.pk)
    friend_request.delet()
    return redirect('friends_list')

    

class FriendsListView(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        friends_list = Friends.objects.filter(Q(current_user_id=current_user.pk) | Q(friend_id=current_user.pk))
        return render(request, 'friendship/friends_list.html',
                       {'profile':profile, 'friends_list':friends_list})
    


def DeleteFriend(request, id):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.pk)
    friend = Friends.objects.get(pk=id)
    friend.delete()
    return redirect('friends_list')




class TodayView(View):
    def get(self, request):
        current_user = request.user
        profile = Profile.objects.get(user_id=current_user.pk)
        today = date.today()
        today = today.weekday()+1
        days = DAYS
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        plan = CurrentPlan.objects.get(current_user_id=current_user.pk)
        exercise_to_plan = ExerciseToPlan.objects.filter(plan_id=plan.plan.id).order_by('day_name')



        return render(request, 'today.html', {'today':today, 'plan':plan, 'days':days, 'exercise_to_plan':exercise_to_plan,'days':days, 'time':time })

        
