from django.contrib.gis.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from django.conf import settings
from django.urls import reverse
import requests
import json
import jdatetime
User = get_user_model()

class Event(models.Model):
    gender_type = (
        ('آقایان', 'آقایان'),
        ('بانوان', 'بانوان'),
    )
    event_list = (
        ('فوتبال','فوتبال'),
        ('تنیس', 'تنیس'),
        ('بسکتبال', 'بسکتبال'),
        ('والیبال', 'والیبال'),
        ('پینتبال', 'پینتبال'),
        ('بازی های کامپیوتری', 'بازی های کامپیوتری'),
        ('شطرنج', 'شطرنج'),
        ('دیگر', 'دیگر'),
    )

    city_list = (
        ('کرج', 'کرج'),
        ('تهران', 'تهران'),
        ('مشهد', 'مشهد'),
        ('اصفهان', 'اصفهان'),
    )
    state_list = (
        ('البرز', 'البرز'),
        ('تهران', 'تهران'),
        ('خراسان شمالی', 'خراسان شمالی'),
        ('اصفهان', 'اصفهان'),
    )
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
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='created', null=True)
    saloon_name = models.CharField(null=True, max_length=20)
    event_name = models.CharField(max_length=15, null=True,blank=True)
    Event_type = models.CharField(max_length=35,
                                  null=True, choices=event_list,blank=True)
    gender = models.CharField(max_length=30, null=True, choices=gender_type,blank=True)
    state=models.CharField(max_length=30,null=True,choices=state_list,blank=True)
    City = models.CharField(null=True, max_length=30, choices=city_list,blank=True)
    address = models.TextField(max_length=100, null=True,blank=True)
    objects = jmodels.jManager()
    date = jmodels.jDateField(null=True)
    time=models.CharField(max_length=15,null=True)
    period_of_time=models.IntegerField(null=True)
    Description = models.TextField(max_length=700, null=True,blank=True)
    Possibilities = MultiSelectField(max_length=200, null=True, choices=possibilitiesـlist,blank=True)
    total = models.IntegerField(null=True,blank=True)
    needed = models.IntegerField(null=True,blank=True)
    total_cost = models.IntegerField(null=True,blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)



    def for_you(self):
        you=int(self.total_cost/self.total)
        return you

    def NOW(self):
       t=jdatetime.datetime.now()
       day=t.day
       return day

    def NOW_month(self):
       t=jdatetime.datetime.now()
       month=t.month
       return month

    def now(self):
       t=jdatetime.datetime.now()
       return t         

    def __str__(self):
        return 'نام :'+self.event_name+" سالن :"+self.saloon_name 

    def default_image(self):
        return self.image.url if self.image else settings.DEFAULT_IMG

    def search_salon(self):
        url = 'https://api.neshan.org/v1/search?term={salon_name}&lat=35.83266&lng=50.99155'.format(
            salon_name=self.saloon_name)
        header = {
            'Api-Key': ''
        }
        resspon = requests.get(url, headers=header)

        t = resspon.json()['items']
        
        for x in t:

            if x['region'].startswith('karaj'):
                return(x)
          
    def get_absolute_url(self):
       return reverse('event_detail',args=(self.pk,))       

    

    def img_type(self):
        if self.Event_type == 'فوتبال':
            return 'http://127.0.0.1:8000/static/app_event/img/football.jpg'
        elif self.Event_type == 'تنیس':
            return 'http://127.0.0.1:8000/static/app_event/img/tennis.jpeg'
        elif self.Event_type == 'بسکتبال':
            return 'http://127.0.0.1:8000/static/app_event/img/basketball.jpg'
        elif self.Event_type == 'والیبال':
            return 'http://127.0.0.1:8000/static/app_event/img/valleyball.jpg'
        elif self.Event_type == 'پینتبال':
            return 'http://127.0.0.1:8000/static/app_event/img/paintball.jpg'
        elif self.Event_type == 'شطرنج':
            return 'http://127.0.0.1:8000/static/app_event/img/chess.jpg'
        elif self.Event_type == 'بازی های کامپیوتری':
            return 'http://127.0.0.1:8000/static/app_event/img/game.jpg'
        elif self.Event_type == 'دیگر':
            return 'http://127.0.0.1:8000/static/app_event/img/other.png'


class messages(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    resiver=models.ForeignKey(Event,null=True,on_delete=models.CASCADE,related_name='message')
    message=models.CharField(max_length=300,null=True,blank=True)
    send_time=jmodels.jDateTimeField(auto_now_add=True,null=True)
    



    class Meta:
        verbose_name_plural=('پیام ها')




    def get_absolute_url(self):
       return reverse('message',args(self.pk,))    
        
    def message_url(self):
        return reverse('messages',args=(self.pk,))    
    

class Confrim(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        event=models.ForeignKey(Event,on_delete=models.CASCADE,null=True,related_name='confrim')
        text=models.CharField(max_length=100,null=True,blank=True)
        create_date_time=models.DateTimeField(auto_now_add=True,null=True)
        approved=models.BooleanField(default=False)

  
        def approve(self):
          self.approved=True
          self.save()


        def __str__(self):
             return self.text

        
class Support(models.Model):
    bl=(
        ("راهنمایی","راهنمایی"),
        ("همکاری","همکاری"),
        ("مدیریت","مدیریت"),
        ("سایر موارد","سایر موارد"),


        )
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50,null=True)
    message=models.TextField(null=True)
    block=models.CharField(max_length=100,null=True,choices=bl)
    answer=models.TextField(null=True,blank=True)
    datetime=jmodels.jDateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return "کاربر:"+""+self.user.username +""+" بخش:"+""+ self.block
    class Meta:
        verbose_name_plural=('پشتیبانی')

    
    def get_absolute_url(self):
      return reverse('tickets',args=(self.pk,))

class Answer(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     ticket=models.ForeignKey(Support,on_delete=models.CASCADE,null=True,related_name='tic')
     answer=models.TextField(null=True)
     datetime=jmodels.jDateTimeField(auto_now_add=True,null=True)


     def __str__(self):
        return 'user'+':'+self.ticket.user.username +''+'title'+':'+self.ticket.title

     class Meta:
        verbose_name_plural=('پاسخ')             



