from django.urls import path
from .views import UserView, PostView

urlpatterns = [
    path('user/<str:action>/', UserView.as_view(), name='user_actions'),
    path('post/<str:action>/', PostView.as_view(), name='post_actions'),
]
