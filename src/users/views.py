from rest_framework.views import APIView
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated

from src.users.serializer import UserRegistrationSerializer, UserSerializer, UserUpdateSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get current user info",
        responses={200: UserSerializer}
    )
    def get(self, request: Request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update user info",
        request_body=UserUpdateSerializer,
        responses={200: UserSerializer}
    )
    def patch(self, request: Request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        if serializer.errors:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
