from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            user_to_follow = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            user_to_unfollow = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {username}."}, status=status.HTTP_200_OK)

