from django.urls import path

from .views import DetailListView, DetailDetailsView, StoryListView, StoryDetailsView

urlpatterns = [
    path('details/', DetailListView.as_view()),
    path('details/<pk>', DetailDetailsView.as_view()),
    path('story/', StoryListView.as_view()),
    path('story/<pk>', StoryDetailsView.as_view()),
]
