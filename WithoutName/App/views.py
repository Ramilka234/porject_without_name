from rest_framework import generics, viewsets
from django.shortcuts import render

from .models import Game
from .serializers import GameListSerializer, GameDetailSerializer, ReviewCreateSerializer


class GameListView(viewsets.ReadOnlyModelViewSet):
    """вывод списка фильмов"""
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDetailView(viewsets.ReadOnlyModelViewSet):
    """Вывод полной игры"""
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewCreateSerializer
