from django.contrib.sitemaps import Sitemap
from app_event.models import Event
from app_blog.models import Blog,Landing
from app_reserve.models import Reserve




class BlogSitemap(Sitemap):
   changefreq = "monthly"
   priority = 0.9
   def items(self):
      return Blog.objects.all()
   def lastmod(self,obj):
     return obj.create_time
      

class EventSitemap(Sitemap):
       def items(self):
           return Event.objects.all()
       def lastmod(self, obj):
          return obj.datetime

     

class ReserveSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.9
  def items(self):
      return Reserve.objects.all()
  def lsatmod(self,obj):
     return obj.datetime    

