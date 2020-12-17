from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User 
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.db.models import Q
import requests
class CustomAuthentication(BasicAuthentication):
    def authenticate(self,request):
        if request.method=="GET":
            username=request.GET.get('user')
            password=request.GET.get('password')
        else:    
            username=request.POST.get("user")
            password=request.POST.get("password")        
        if username is None:
            return None
        try:
            user=authenticate(username=username,password=password)
            if user is None:
                user=User.objects.get(Q(username=username)& Q(password=password))
        except:
            raise AuthenticationFailed("Please login")
        return(user,None)    