from rest_framework import generics, permissions, viewsets
from .models import Notes
from .serializers import NotesSerializer
from socializer_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


class NotesListView(viewsets.ModelViewSet):
    """View for listing and creating notes."""
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting notes."""
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
