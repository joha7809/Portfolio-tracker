from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='api-logout'),
    path('login/', LoginView.as_view(), name='api-login'),
]
