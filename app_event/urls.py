from django.conf.urls import url
from django.urls import path, include
from app_event import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.event_func, name='event'),
    path('event-category/',views.event_cat,name='cat'),
    path('search/',views.search_event,name='search'),
    path('404/', views.not_find, name='not_find'),
    path('new/',views.new,name='new'),
    path('new-event/',views.new_event, name='new_event'),
    path('event-detail/<int:pk>/',views.event_detail,name='event_detail'),
    path('event-edit/<int:pk>/',views.event_edit,name='event-edit'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('event-detail/confrim/<int:pk>',views.confrim_event,name='confrim'),
    path('event-detail/message/<int:pk>/',views.message,name='message'),
    path('event-detail/message/<int:pk>/chat-room',views.chat_room,name='chat'),
    path('inbox/',views.inbox,name='inbox'),
    path('confrim/<int:pk>/approve/',views.approve,name='approve'),
    path('confrim/<int:pk>/delete_approve/',views.delete_approve,name='delete_approve'),
    path('user-list/<int:pk>/',views.user_list,name='user-list'),
    path('event-detail/<int:pk>/remove/',views.remove_event,name='remove_event'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('my-events/',views.my_events,name='my_events'),
    path('my-events/expire/',views.expire,name='expire'),
    path('my-events/waiting/',views.waiting,name='waiting'),
    path('landing/<str:slug>/',views.landing,name='landing'),
   

]
