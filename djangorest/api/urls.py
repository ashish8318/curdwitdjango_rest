
from django.urls import path,include
from .import views

urlpatterns = [
    path('login/',views.login.as_view()),
    path('list/', views.userList.as_view()),
    path('details/<int:pk>/',views.userDetail.as_view()),
    path('create/',views.create.as_view()),
    path('delete/<int:pk>/',views.userDelete.as_view()),
    path('loginapi/',views.login.as_view())
    
]
