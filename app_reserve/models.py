from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django_jalali.db import models as jmodels
from django.urls import reverse
from django_jalali.db import models as jmodels
my_validator = RegexValidator(
    r"^[0][9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$")


class Reserve(models.Model):




    possibilitiesـlist = (
        ('بوفه', 'بوفه'),
        ('سرویس بهداشتی', 'سرویس بهداشتی'),
        ('دوش و کمد', 'دوش و کمد'),
        ('رختکن', 'رختکن'),
        ('پارکینگ', 'پارکینگ'),
        ('فروشگاه', 'فروشگاه'),
        ('تهویه هوا', 'تهویه هوا'),
        ('فضای سبز', 'فضای سبز'),
        ('ماساژ', 'ماساژ'),
        ('جایگاه تماشاچیان', 'جایگاه تماشاچیان'),
        ('توپ', 'توپ'),
        ('مربی', 'مربی'),

    )

    salon_name = models.CharField(max_length=80, null=True,blank=True)
    manager_name = models.CharField(max_length=30, null=True,blank=True)
    phone_number = models.CharField(
        max_length=12, null=True,blank=True)
    city = models.CharField(max_length=60, null=True,blank=True)
    address = models.CharField(max_length=160, null=True,blank=True)
    salon_type = models.CharField(max_length=30, null=True,blank=True)
    salon_roof=models.CharField(max_length=30,null=True,blank=True)
    salon_sport=models.CharField(max_length=160,null=True,blank=True)
    gender = models.CharField(max_length=15, null=True,blank=True)
    Possibilities = MultiSelectField(max_length=120, null=True, choices=possibilitiesـlist,blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    cash=models.IntegerField(null=True,blank=True)
    instagram=models.URLField(null=True,blank=True)
    burn=models.CharField(max_length=30,null=True,blank=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True)
 


   
    def __str__(self):
        return self.salon_name

    def get_absolute_url(self):
       return reverse('salon_detail' ,args=(self.salon_name,))    

    
    def salon_image(self):
      if self.salon_type == 'سالن ':
        return 'http://hamtimi.ir/static/app_event/img/football.jpg'
      elif self.salon_type == 'زمین چمن مصنوعی':
        return 'http://hamtimi.ir/static/app_event/img/chaman_m.jpg'
      elif self.salon_type == 'باشگاه':
        return 'http://hamtimi.ir/static/app_event/img/multi.jpg'
      elif self.salon_type == 'چمن':
        return 'http://hamtimi.ir/static/app_event/img/chaman.jpg'
      elif self.salon_type == 'سوارکاری':
        return 'http://hamtimi.ir/static/app_event/img/savar.jpg'
      elif self.salon_type == 'استخر':
        return 'http://hamtimi.ir/static/app_event/img/pool.jpg'
      elif self.salon_type == 'مجموعه ورزشی':
        return 'http://hamtimi.ir/static/app_event/img/multi.jpg'
      elif self.salon_type == 'مدرسه فوتبال':
        return 'http://hamtimi.ir/static/app_event/img/madrese.jpg'     

class Comment_Salon(models.Model):
  user=models.CharField(max_length=20,null=True)
  email=models.EmailField(max_length=50,null=True,blank=True)
  salon=models.ForeignKey(Reserve,on_delete=models.SET_NULL,null=True,related_name='cm')
  message=models.CharField(max_length=150,null=True)
  star=models.CharField(max_length=10,null=True,blank=True)
  created_time=jmodels.jDateTimeField(auto_now_add=True,null=True)


  def __str__(self):
     return self.user +''+self.salon         
  
  def get_absolute_url(self):
    return reverse('salon_comment',args(self.salon_name,))

