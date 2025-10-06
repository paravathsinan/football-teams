from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/',views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('explore/', views.explore, name='explore'),
    path('add/', views.add_team, name='add'),
]
