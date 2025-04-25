from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Only allow logout if logged in

    def post(self, request):
        logout(request)
        response = Response({'detail': 'Logged out successfully.'}, status=status.HTTP_200_OK)
        response.delete_cookie('sessionid')  # Optional: delete sessionid manually
        return response
