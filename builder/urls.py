from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'builder'
urlpatterns = [
    path('search/<str:username>', views.search, name='search'),
    path('',views.signup, name = 'home'),
    path('signin/',views.signin, name= 'signin'),
    path('showlist/' ,views.showlist, name ='showlist' ),
]
