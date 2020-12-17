from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
import requests
import json

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        params={'user':username,'password':password}
        r=requests.get("http://127.0.0.1:8000/api/loginapi/",params=params)
        if r.status_code==200:
            request.session['is_name']=username
            request.session['is_password']=password
            r=requests.get("http://127.0.0.1:8000/api/list/",{"user":username,"password":password})
            alluser=r.json()
            print(alluser)
            return render(request,"home.html",{"username":username,"alluser":alluser})
        else:
            messages.error(request,"Please Enter correct data")
            return redirect("login")
    else:
        return render(request,"login.html")

def register(request):
    if request.method=='POST':
        data={'username':request.POST["username"],'email':request.POST["email"],'password':request.POST["password"],'csrfmiddlewaretoken':request.POST["csrfmiddlewaretoken"]}
        r=requests.post("http://127.0.0.1:8000/api/create/",data=data)
        print(r.json())
        if r.status_code==201:
            messages.success(request,"User account created")
            return redirect('login')
        else:
           messages.error(request,"Something is worng")     
           return render(request,"home.html")
    u=User.objects.all()
    for i in u:
        print(i.password)
    messages.error(request,"Please register now")
    return render(request,"home.html")      

def getdetails(request,id):
    username=request.session.get("is_name")
    password=request.session.get("is_password")
    r1=requests.get("http://127.0.0.1:8000/api/details/"+str(id),{"user":username,"password":password})
    r2=requests.get("http://127.0.0.1:8000/api/list/",{"user":username,"password":password})
    alluser=r2.json()
    userdata=r1.json()
    messages.success(request,"Please update data")
    return render(request,"home.html",{"username":username,"alluser":alluser,"userdata":userdata})

def update(request):
    oldusername=request.session.get("is_name")
    password=request.session.get("is_password")
    print(oldusername)
    id=request.POST['id']
    print(id)
    data={"username":request.POST["username"],"email":request.POST["email"],'csrfmiddlewaretoken':request.POST["csrfmiddlewaretoken"],"user":oldusername,"password":password}
    r=requests.patch("http://127.0.0.1:8000/api/details/"+id+"/",data=data)
    if r.status_code==200:
        del request.session["is_name"]
        del request.session["is_password"]
        messages.success(request,"your name and email updateted")
        return redirect("login")
   
def delete(request,id):
    username=request.session.get("is_name")
    password=request.session.get("is_password")
    r=requests.delete("http://127.0.0.1:8000/api/delete/"+str(id))
    if r.status_code==204:
        r2=requests.get("http://127.0.0.1:8000/api/list/",{"user":username,"password":password})
        if r2.status_code==200:
            alluser=r2.json()
            messages.success(request,"Delete success")
            return render(request,"home.html",{"username":username,"alluser":alluser})
        else:
            messages.success(request,"Please login other user")    
            return redirect("login")
     

def logout(request):
    del request.session["is_name"]
    del request.session["is_password"]
    messages.success(request,"Succcessfuly logout")
    return redirect("login")      