from django.conf.urls import url
from django.urls import path, include
from app_blog import views




urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:title>',views.blog_post,name='post'),
    path('<str:title>/comment/',views.comment,name='comment'),
    path('<str:title>/rep-comment/',views.rep_comment,name='rep'),
 


]
