from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('user/<user_id>', views.profile, name='profile'),
    path('user/update/profile', views.update_profile, name='updateprofile'),
]