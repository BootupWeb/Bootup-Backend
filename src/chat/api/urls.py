from django.urls import path

from .views import ChatListView, ChatDetailsView

urlpatterns = [
    path('chat/', ChatListView.as_view()),
    path('chat/<pk>/', ChatDetailsView.as_view()),
]
