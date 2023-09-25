from django.urls import path
from .views import UserRegistrationView, CurrentUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('', CurrentUserView.as_view(), name='user_info'),
]
