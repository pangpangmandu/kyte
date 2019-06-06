from django.urls import path
from match import views

urlpatterns = [
    path('', views.index , name="main"),
    path('gameselect/', views.gameselect, name= "gameselect"),
    path('gamesearch/', views.gamesearch, name="gamesearch"),
    path('result/', views.result, name="result"),
    path('mypage/', views.mypage, name="mypage"),
    path('gameadd/', views.gameadd, name="gameadd"),
]
