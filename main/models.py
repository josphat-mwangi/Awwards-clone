from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.TextField(max_length=500, blank=True)
    post = models.ForeignKey('Project', on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=CASCADE)

class Project(models.Model):
    author = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    link = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    design = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)

class Contact(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
