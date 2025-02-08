from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="blog-index"),
    path('post_details/<int:pk>', views.post_detail, name="blog-post-detail"),
    path('post_edit/<int:pk>', views.post_edit, name="blog-post-edit"),

    path('post_delete/<int:pk>', views.post_delete, name="blog-post-delete"),

    path('post/<int:pk>/comment/<int:pk1>/delete', views.comment_delete, name="comment-delete"),
]  