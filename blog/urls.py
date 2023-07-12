from django.urls import path

from .views import BlogPostView, BlogDetailView # new

urlpatterns = [
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
]
