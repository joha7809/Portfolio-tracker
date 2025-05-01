from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from .serializers import LoginSerializer
from .serializers import UserSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Only allow logout if logged in

    def post(self, request):
        logout(request)
        response = Response(
            {"detail": "Logged out successfully."}, status=status.HTTP_200_OK
        )
        # Optional: delete sessionid manually
        response.delete_cookie("sessionid")
        return response


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            user_data = UserSerializer(user).data
            response = Response(
                {"detail": "Logged in successfully.", "user": user_data},
                status=status.HTTP_200_OK,
            )
            # response.set_cookie('sessionid', request.COOKIES.get('sessionid'), httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
