from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Friend
from .serializers import FriendSerializer

class FriendList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, friend=self.kwargs['pk'])

class FriendDetail(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    # Path: friends/urls.py
