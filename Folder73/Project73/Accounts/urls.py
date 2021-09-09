from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signUpView,name='signup'),
    path('signin/',views.signInView,name='signin'),
    path('signout/',views.signOutView,name='signout')
]