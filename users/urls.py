from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('grid/', views.grid, name='grid'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('editprofile/<slug:slug>/', views.ProfileUpdate.as_view(), name='editprofile'),
    path('postdetail/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('like/<uuid:post_id>/', views.likes, name='likes'),
    path('twister/', views.twister, name='twister'),
    # path('newpost/posted/', views.new_post, name='newpost')
    # path('srtd/<int:pk>/', views.anon, name='anon')
]
