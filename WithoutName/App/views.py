from rest_framework import generics, viewsets, status, mixins
from django.shortcuts import render
from rest_framework.response import Response

from .models import Game
from .serializers import GameListSerializer, GameDetailSerializer, ReviewCreateSerializer, \
    GameCreateSerializer, GameEditOrDeleteSerializer


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


class GameCreateView(viewsets.ModelViewSet):
    serializer_class = GameCreateSerializer


class GameDeleteOrUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameEditOrDeleteSerializer

