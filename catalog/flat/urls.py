from django.urls import path

from . import views

urlpatterns = [
     path('', views.posts, name="posts"),
    path('posts/<int:post_id>/', views.posts_view, name="posts"),
    path("create_post/", views.create_post, name="create_post"),
path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("<int:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
    ]