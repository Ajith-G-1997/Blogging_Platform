from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from .views import (
    UserRegistrationView,
    AddPost,
    PostDetailView,
    CommentList,
    CommentDetailView,
    AdminRegisterView,
    AdminPostListView,
    AdminPostDetailView,
    AdminCommentListView,
    AdminCommentDetailView
   
)

urlpatterns = [
    # URLs for User Section
    path('users/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('addpost/',AddPost.as_view(),name='addpost'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='PostDetailView'),
    path('CommentList/',CommentList.as_view(),name='CommentList'),
    path('CommentList/<int:pk>/',CommentDetailView.as_view(),name='CommentDetailView'),
    path('admin/register/', AdminRegisterView.as_view(), name='admin-register'),
    path('admin/posts/', AdminPostListView.as_view(), name='admin-post-list'),
    path('admin/posts/<int:pk>/', AdminPostDetailView.as_view(), name='admin-post-detail'),
    path('admin/comments/', AdminCommentListView.as_view(), name='admin-comment-list'),
    path('admin/comments/<int:pk>/', AdminCommentDetailView.as_view(), name='admin-comment-detail'),
 
    

    
]
