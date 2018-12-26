from django.urls import path

from .views import CredentialListView, CredentialDetailsView
from .views import ProfileListView, ProfileDetailsView
from .views import RoleListView, RoleDetailsView

urlpatterns = [
    path('user/', CredentialListView.as_view()),
    path('user/<pk>', CredentialDetailsView.as_view()),
    path('profile/', ProfileListView.as_view()),
    path('profile/<pk>', ProfileDetailsView.as_view()),
    path('role/', RoleListView.as_view()),
    path('role/<pk>', RoleDetailsView.as_view()),
]
