from rest_framework import generics, permissions
from socializer_api.permissions import IsOwnerOrReadOnly
from .models import Messages
from .serializers import MessagesSerializer, MessagesDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MessageList(generics.ListCreateAPIView):
    """
    List messages or create a message if logged in.
    """
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Messages.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a message, or update or delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MessagesDetailSerializer
    queryset = Messages.objects.all()
