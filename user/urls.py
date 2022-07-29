from django.urls import path

from user.views import *

urlpatterns = [
    path('', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),
    path('logout/', Logout.as_view(), name="logout"),
    # path('userdetail/', UserDetailView.as_view(), name="user_detail"),



]