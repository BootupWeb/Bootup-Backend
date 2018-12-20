from django.urls import path

from .views import CredentialListView, CredentialDetailsView

urlpatterns = [
    path('', CredentialListView.as_view()),
    path('<pk>', CredentialDetailsView.as_view()),
]
