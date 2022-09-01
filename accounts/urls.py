from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'), 
    path('login/', LoginView.as_view(), name='login'), 
    path('profile/<str:username>/', userProfileView, name='profile'), 
    path('edit-profile/', userProfileEditView, name='edit_profile'), 
]