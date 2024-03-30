from rest_framework import generics, permissions
from socializer_api.permissions import IsOwnerOrReadOnly
from .models import Messages, Chat
from .serializers import MessagesSerializer, MessagesDetailSerializer, ChatSerializer, ChatDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ChatList(generics.ListCreateAPIView):
    """
    List chats or create a chat if logged in.
    """
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chat.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user1', 'user2']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a chat, or update or delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatDetailSerializer
    queryset = Chat.objects.all()


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
