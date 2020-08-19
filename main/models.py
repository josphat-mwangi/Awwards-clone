from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.TextField(max_length=500, blank=True)
    pub_date =models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.filter(user = id)
        latest_profile = profile.order_by('-pub_date').first()
        return latest_profile


    

class Project(models.Model):
    author = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='image/')
    description = HTMLField()
    link = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title



class Rating(models.Model):
    design = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)

class Contact(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
