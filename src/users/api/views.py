from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.contrib.auth.models import User

from users.models import Profile, Role
from .serializers import UserSerializer, ProfileSerializer, RoleSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetailsView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
