
from rest_framework import views, status
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .serializers import UserSerializer


class LoginApiView(views.APIView):
    def post(self, request):

        user = authenticate(username=request.data.get("username"),
                            password=request.data.get("password"))
        if user is None:
            return Response({
                'message':
                'sorry we could not authenticate the user with the details provided'},
                status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)

        return Response(UserSerializer(user).data)
