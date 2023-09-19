from django.urls import path

from .views import GameListView, GameDetailView, ReviewCreateViewSet, GameCreateView, \
    GameDeleteOrUpdateView

urlpatterns = [
    path('game/', GameListView.as_view({'get': 'list'})),
    path('game/<int:pk>/', GameDetailView.as_view({'get': 'retrieve'})),
    path('review/', ReviewCreateViewSet.as_view({'post': 'create'})),
    path('game/create/',  GameCreateView.as_view({'post': 'create'})),
    path('game/<int:pk>/edit-delete/', GameDeleteOrUpdateView.as_view(), name='game-edit-delete'),
]

