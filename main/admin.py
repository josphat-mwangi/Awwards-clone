from django.contrib import admin
from .models import Profile,Project,Rating,Contact
# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Contact)
