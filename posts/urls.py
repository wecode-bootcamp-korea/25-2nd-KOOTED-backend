from django.urls import path

from .views import PostsView, PostDetailView, BookMarkView

urlpatterns = [
    path('', PostsView.as_view()),
    path('/<int:post_id>', PostDetailView.as_view()),
    path('/bookmarks', BookMarkView.as_view()),
]