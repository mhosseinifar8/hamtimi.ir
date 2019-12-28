"""hamtimi_beta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from app_event import views
from django.contrib.sitemaps.views import sitemap
from hamtimi_beta.sitemaps import EventSitemap,BlogSitemap,ReserveSitemap
sitemaps = {
    'event':EventSitemap,'blog':BlogSitemap,'salon':ReserveSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',include('app_blog.urls')),
    path('event/',include('app_event.urls')),
    path('accounts/',include('app_profile.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('reserve/',include('app_reserve.urls')),
    path('dashboard/',include('app_event.urls')),
    path('support/',views.support,name='support'),
    path('answer/',views.answer,name='answer'),
    path('all-ticket/',views.all_ticket,name='all_ticket'),
    path('tickets/<int:pk>/',views.tickets,name='tickets'),
    path('about-us/',views.about_us,name='about'),
    path('privacy/',views.privacy,name='privacy'),
    path('search-blog/',views.search_blog,name='search_blog'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('search-salon/',views.search_salon,name='search_salon'),
    url(r'^froala_editor/', include('froala_editor.urls')),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)