from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(ModelViewSet):
    def post(self , request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response( { "status":"success" , 'refresh': str(refresh),
                           'access': str(refresh.access_token) })

