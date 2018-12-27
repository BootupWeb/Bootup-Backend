from django.contrib import admin

# Register your models here.
from .models import Detail, Story, Update

admin.site.register(Detail)
admin.site.register(Story)
admin.site.register(Update)
