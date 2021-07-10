from django.urls import path
from user import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/',views.register_view,name= 'register' ),
    path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',views.profile_view,name='profile')
]