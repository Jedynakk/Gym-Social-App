from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    height = models.PositiveIntegerField(default=0, null=True)
    weight = models.PositiveIntegerField(default=0, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/profpic.png')
    bio = models.TextField(null=True)
 

    def profile_username(self):
        username = self.user.username
        return username
    
    @property
    def image_url(self):
        if self.profile_image and hasattr(self.image, 'url'):
            return self.profile_image.url

class Friends(models.Model):
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, related_name="current_user")
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, related_name="friend")
    

class RequestFriends(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, related_name="request_from")
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, related_name="recipient")
    sent = models.DateField(auto_now_add=True)


class Post(models.Model):
    author =  models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    

    @property
    def CountLikes(self):
        post = self.pk
        likes = LikePost.objects.filter(post_id=post).count()
        return likes





class LikePost(models.Model):
    current_user =  models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
