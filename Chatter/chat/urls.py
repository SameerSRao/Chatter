from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('history/<str:room_name>/', views.chat_history, name='chat_history'),
    path("chat/<str:room_name>/", views.room, name="room"),
    path('chat/<str:room_name>/leave/', views.leave_room, name='leave_room'),
    path('owned-rooms/', views.owned_rooms_view, name='owned_rooms'),
]
