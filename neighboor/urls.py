from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('user/<user_id>', views.profile, name='profile'),
    path('user/update/profile', views.update_profile, name='updateprofile'),
    path('neighbourhood/<neighbourhood_id>',views.neighborhood,name='neighbourhood'),
    path('joinhood/<neighbourhood_id',views.join_hood,name="joinhood"),
    path('leavehood/<neighbourhood_id',views.leave_hood,name="leavehood")
]