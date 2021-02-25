from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime
from users.models import Profile
from django.dispatch import receiver
from django.utils.text import slugify

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Title', max_length=500, blank=False, null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    about = models.TextField('About', max_length=5000)
    image = models.ImageField(upload_to='img/post_content', default='static/def_user.jpg', null=False, blank=False)
    file = models.FileField('File', upload_to='file/post_content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)



    def __str__(self):
        return self.title

    def get_comment_url(self):
        return reverse('users:post_detail', args=[self.id])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created', )

class Twister(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='twisters')
    body = models.TextField('About', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.id)

    class Meta:
        verbose_name = 'Twister'
        verbose_name_plural = 'Twisters'
        ordering = ('-created',)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField("Comment's body")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.post}-{self.author}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created',)

class Likes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'post_likes')
    active = models.BooleanField(default=False)

class Views(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'user_views')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'post_views')
