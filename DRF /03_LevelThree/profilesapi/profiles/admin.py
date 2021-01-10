from django.contrib import admin
from profiles.models import ProfileStatus, Profile
# Register your models here.
admin.site.register([Profile,ProfileStatus])
