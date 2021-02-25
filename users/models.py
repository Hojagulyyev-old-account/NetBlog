from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

def u_d_p(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, instance.user.id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    avatar = models.ImageField('Avatar', upload_to=u_d_p, blank=True, null=True, default='static/img/def_user.jpg')
    bio = models.TextField('Bio', max_length=1500, default='No Biography Yet')
    slogan = models.CharField('Slogan', max_length=300, default='You can if you think you can !')
    # direction = models.ManyToManyField('directions.Direction', related_name='profiles')
    birthday = models.DateField(default=datetime.datetime(2002, 1, 1, 1, 1, 1, 1))
    slug = models.SlugField('Slug', default=user, unique = True, null = False)
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_editprofile_url(self):
        return reverse("{% url 'users:editprofile' %}", args=[str(self.slug)])

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('created', )
