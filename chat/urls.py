from django.urls import path
from chat import views

urlpatterns = [
    path('chat/', views.ChatList.as_view()),
    path('chat/<int:pk>/', views.ChatDetail.as_view()),
    path('chat/messages/', views.MessageList.as_view()),
    path('chat/<int:chat_id>/messages/<int:pk>/', views.MessageDetail.as_view()),
]
