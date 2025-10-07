from django.urls import path
from blog.views import PostView, PostDetail


urlpatterns = [
    path("home/", PostView.as_view(), name="home"),
    path("", PostView.as_view(), name="index"),
    path("<slug:slug>/", PostDetail.as_view(), name="post-detail"),
]
