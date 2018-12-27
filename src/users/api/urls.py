from django.urls import path

from .views import CredentialListView, CredentialDetailsView
from .views import ProfileListView, ProfileDetailsView
from .views import FounderListView, FounderDetailsView
from .views import InvestorListView, InvestorDetailsView

urlpatterns = [
    path('user/', CredentialListView.as_view()),
    path('user/<pk>', CredentialDetailsView.as_view()),
    path('profile/', ProfileListView.as_view()),
    path('profile/<pk>', ProfileDetailsView.as_view()),
    path('founder/', FounderListView.as_view()),
    path('founder/<pk>', FounderDetailsView.as_view()),
    path('investor/', InvestorListView.as_view()),
    path('investor/<pk>', InvestorDetailsView.as_view()),
]
