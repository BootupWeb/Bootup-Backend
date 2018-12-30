from django.urls import path

from .views import ChatListView, ChatDetailsView
from .views import MessageListView, MessageDetailsView

urlpatterns = [
    path('chat/', ChatListView.as_view()),
    path('chat/<pk>/', ChatDetailsView.as_view()),
    path('message/', MessageListView.as_view()),
    path('message/<pk>/', MessageDetailsView.as_view()),
]
