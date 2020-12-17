from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('getdetails/<int:id>/',views.getdetails,name="getdetails"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('logout/',views.logout,name="logout"),
    path('update/',views.update,name="update")
]