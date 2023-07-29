# blog/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import  Comment, User,Post
from .serializers import PostSerializer, CommentSerializer, UserSerializer,AdminRegisterSerializer
from .permissions import IsAuthorOrReadOnly, IsAdminUser
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny



#----------------------------------Start User Section--------------------------------------

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = response.data
        subject = 'Welcome to our Blogging Platform'
        message = f'Hi {user["username"]},\n\nThank you for registering on our Blogging Platform. We hope you enjoy your blogging experience!\n\nBest regards,\nThe Blogging Platform Team'
        from_email = 'your_email@example.com'  # Update this with your email address
        recipient_list = [user['email']]
        send_mail(subject, message, from_email, recipient_list)
        return response

class AddPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['created_user'] = request.user.id
        response = super().post(request, *args, **kwargs)
        return Response({"message": "New Post created Successfully"})
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['created_user'] = request.user.id
        response = super().post(request, *args, **kwargs)
        return Response({"message": "New Comment created Successfully"})

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#----------------------------------End User Section--------------------------------------


#-----------------------------------Admin Section----------------------------------------- 

class AdminRegisterView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = AdminRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Admin User created."}, status=201)

class AdminPostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class AdminPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response({'message': 'Post is deleted'})

class AdminCommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class AdminCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response({'message': 'Comment is deleted'})