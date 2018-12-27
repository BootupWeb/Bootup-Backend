from django.urls import path

from .views import DetailListView, DetailDetailsView, StoryListView, StoryDetailsView
from .views import UpdateListView, UpdateDetailsView

urlpatterns = [
    path('details/', DetailListView.as_view()),
    path('details/<pk>', DetailDetailsView.as_view()),
    path('story/', StoryListView.as_view()),
    path('story/<pk>', StoryDetailsView.as_view()),
    path('update/', UpdateListView.as_view()),
    path('update/<pk>', UpdateDetailsView.as_view())
]
