from django.urls import path
from . import views
from .views import (PostList, PostDetail, PostLike, CreatePost,
                    DeletePost, UpdatePost)


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('postcreate/', CreatePost.as_view(), name='createpost'),
    path('postdelete/<int:pk>', DeletePost.as_view(), name='deletepost'),
    path('postupdate/<int:pk>', UpdatePost.as_view(), name='updatepost'),
    path('item/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
