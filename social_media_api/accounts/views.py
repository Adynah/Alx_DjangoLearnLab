from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=self.object)
        response.data['token'] = token.key
        return response
