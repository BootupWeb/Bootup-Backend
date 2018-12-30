from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', include('users.api.urls')),
    path('api/campaign/', include('campaign.api.urls')),
    path('api/chat/', include('chat.api.urls'))
]
