from django.urls import path

from .views import DetailListView, DetailDetailsView

urlpatterns = [
    path('details/', DetailListView.as_view()),
    path('details/<pk>', DetailDetailsView.as_view()),
]
