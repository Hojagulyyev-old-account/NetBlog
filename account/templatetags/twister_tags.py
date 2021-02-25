from django import template
from users.models import Profile
from posts.models import Twister, Post


register = template.Library()

@register.inclusion_tag('users/twisters/twisters.html')
def show_twisters():
    twisters = Twister.objects.all()[:2]
    return {'twisters':twisters}

@register.inclusion_tag('users/twisters/twisters2.html')
def show_twisters2():
    twisters = Twister.objects.all()[2:4]
    return {'twisters':twisters}

@register.inclusion_tag('users/twisters/info.html')
def show_info():
    users = Profile.objects.all().exclude(user__username='admin').count()
    posts = Post.objects.all().count()
    twisters = Twister.objects.all().count()
    return {'twisters':twisters, 'posts':posts, 'users':users}
