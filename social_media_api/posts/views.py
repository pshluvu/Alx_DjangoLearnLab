# accounts/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view

User = get_user_model()


# -------------------------------
# User Registration & Authentication
# -------------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token = user.auth_token.key  # Token created automatically in serializer
        return Response({
            'user': response.data,
            'token': token
        })


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = user.auth_token.get_or_create()
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# -------------------------------
# Follow / Unfollow Functionality
# -------------------------------



@api_view(['POST'])
@permissions.IsAuthenticated
def follow_user(request, user_id):
    try:
        target_user = User.objects.get(id=user_id)
        if request.user == target_user:
            return Response({'error': 'Cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        target_user.followers.add(request.user)
        return Response({'message': f'You are now following {target_user.username}'})
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permissions.IsAuthenticated
def unfollow_user(request, user_id):
    try:
        target_user = User.objects.get(id=user_id)
        if request.user == target_user:
            return Response({'error': 'Cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        target_user.followers.remove(request.user)
        return Response({'message': f'You have unfollowed {target_user.username}'})
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
