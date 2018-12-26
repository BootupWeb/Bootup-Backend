from django.contrib import admin

from .models import Credential, Profile, Role

admin.site.register(Credential)
admin.site.register(Profile)
admin.site.register(Role)
