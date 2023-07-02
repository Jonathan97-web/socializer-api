from rest_framework import generics
from .models import Notes
from .serializers import NotesSerializer, NotesDetailSerializer
from socializer_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


class NotesListView(generics.ListCreateAPIView):
    """View for listing and creating notes."""
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting notes."""
    queryset = Notes.objects.all()
    serializer_class = NotesDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(owner=user)
