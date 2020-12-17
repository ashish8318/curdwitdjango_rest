
from .serilizer import userserilizer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from .customauthentication import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import io
from rest_framework.parsers import JSONParser


class userList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = userserilizer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
    
class create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserilizer

class userDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = userserilizer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]

class userDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userserilizer

class login(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        username=request.GET.get('username')
        # json_data=request.body
        # stream=io.BytesIO(json_data)
        # python_data=JSONParser().parse(stream)
        # print(type(request))
        # # user=authenticate(request,username=python_data['name'],password=python_data['password'])
        # # if user is not None:
        # #     login(request,user)
        # #     print(user)
        # usernames = [user.username for user in User.objects.all()]
        return Response({"username":username})    
        
