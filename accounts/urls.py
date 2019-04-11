from django.conf.urls import include
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]