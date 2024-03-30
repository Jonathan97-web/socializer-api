from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view({None}), name="profile-list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile-detail"),
]