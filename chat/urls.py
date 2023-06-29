from django.urls import path
from chat import views

urlpatterns = [
    path('chat/', views.MessageList.as_view()),
    path('chat/<int:pk>/', views.MessageDetail.as_view()),
]
