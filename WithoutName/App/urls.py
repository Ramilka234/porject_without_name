from django.urls import path

from .views import GameListView, GameDetailView, ReviewCreateViewSet

urlpatterns = [
    path('game/', GameListView.as_view({'get': 'list'})),
    path('game/<int:pk>/', GameDetailView.as_view({'get': 'retrieve'})),
    path('review/', ReviewCreateViewSet.as_view({'post': 'create'}))
]

