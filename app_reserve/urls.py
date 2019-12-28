from django.conf.urls import url
from django.urls import path, include
from app_reserve import views


urlpatterns = [
   

   path('',views.saloon,name='salon'),
   path('salon-detail/<str:salon_name>',views.salon_detail,name='salon_detail'),
   path('salon/comment/<str:salon_name>',views.cm_salon,name='salon_comment'),





]
