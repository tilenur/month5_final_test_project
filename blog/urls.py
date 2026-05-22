from django.urls import path
from . import views


urlpatterns = [
    path(
        'posts/',
        views.PostViewSet.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),

    path(
        'posts/<int:pk>/comments/',
        views.PostCommentListCreateAPIView.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),

    path(
        'posts/<int:pk>/',
        views.PostViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',
        })
    ),

    path(
        'comments/',
        views.CommentViewSet.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),

    path(
        'comments/<int:pk>/',
        views.CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',
        })
    ),
]