from django.urls import path, include

from turret import views

app_name = "turret"

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path("video_feed/", views.video_feed, name="video_feed")
]
