from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('user/', views.profile, name='profile'),
    path('search/', views.search_hood, name='search_hoods'),
    
    path('neighbourhood/<neighborhood_id>',views.neighborhood,name='neighbourhood'),
    path('joinhood/<neighborhood_id>',views.join_hood,name="joinhood"),
    path('leavehood/<neighborhood_id>',views.leave_hood,name="leavehood")
]