"""socializer_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from rest_framework import routers
from profiles.views import ProfileList
from posts.views import PostList
from notes.views import NotesListView
from comments.views import CommentList
from friends.views import FriendList


router = routers.DefaultRouter()
router.register(r'profiles', ProfileList),
router.register(r'posts', PostList)
router.register(r'notes', NotesListView)
router.register(r'comments', CommentList)
router.register(r'friends', FriendList)




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('followers.urls')),
    path('', include('likes.urls')),
    path('', include('comments.urls')),
    path('', include('chat.urls')),
    path('', include('notes.urls'))
]

urlpatterns += router.urls

