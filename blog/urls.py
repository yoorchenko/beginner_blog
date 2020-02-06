from .views import BlogListView, DetailPostView
from django.urls import path

urlpatterns = [
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),  # new
    path('', BlogListView.as_view(), name='home'),
]