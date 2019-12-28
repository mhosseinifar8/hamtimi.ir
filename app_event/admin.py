from django.contrib import admin
from app_event.models import Event,messages,Support,Answer
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget
from app_event.models import Confrim 
class EventAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )


class EventTimeAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )
class CityAdmin(admin.ModelAdmin):
   formfield_overrides = {
     models.PointField: {"widget": GooglePointFieldWidget}
    }
admin.site.register(Event)
admin.site.register(Confrim)
admin.site.register(messages)
admin.site.register(Support)
admin.site.register(Answer)

