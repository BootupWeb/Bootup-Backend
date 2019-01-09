from django.urls import path
from django.contrib.auth.models import User

from .views import UserListView, UserDetailsView
from .views import ProfileListView, ProfileDetailsView
from .views import RoleListView, RoleDetailsView

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<pk>', UserDetailsView.as_view()),
    path('profile/', ProfileListView.as_view()),
    path('profile/<pk>', ProfileDetailsView.as_view()),
    path('role/', RoleListView.as_view()),
    path('role/<pk>', RoleDetailsView.as_view()),
]
