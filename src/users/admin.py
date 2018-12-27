from django.contrib import admin

from .models import Credential, Profile, Founder, Investor

admin.site.register(Credential)
admin.site.register(Profile)
admin.site.register(Founder)
admin.site.register(Investor)
