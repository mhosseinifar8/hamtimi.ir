from django.conf.urls import url
from django.urls import path ,include
from app_profile import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('my-profile/',views.profile,name='my-profile'),
    path('contact/',views.contact,name='contact'),
    path('coming-soon/',views.coming_soon,name='coming_soon'),
    url('^', include('django.contrib.auth.urls')),
    path('signup/',views.signup,name='signup'),
    path('login-user/',views.login_costum,name='loginn'),
    path('authenticate/',views.confrim_number,name='authenticate'),
    path('authenticate/verify/',views.verify_phone,name='acc'),
    path('signout/', views.signout, name='signout'),
    path('<str:username>/', views.account, name='profile'),
    path('auth/', include('social_django.urls', namespace='social')),
 
]