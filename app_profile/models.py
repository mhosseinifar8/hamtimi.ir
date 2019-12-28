from django.db import models
from app_event.models import Event
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_jalali.db import models as jmodels
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.urls import reverse
from multiselectfield import MultiSelectField
ddd = get_user_model()



def get_upload_path(instance, filename):
    return 'user/{username}/{filename}'.format(
        username=instance.user.username,
        filename=filename
    )
class UserProfileManager(models.Manager):
         pass

class Profile(models.Model):
    gender_list = (
        ('مرد','مرد'),
        ('زن','زن'),
    )


    city_list = (
        ('تهران','تهران'),
        ('کرج','کرج'),
        ('مشهد','مشهد'),
        ('تبریز','تبریز'),
        ('اصفهان','اصفهان'),
        ('شیراز','شیراز'),
    )

    fav_list = (
        ('فوتبال','فوتبال'),
        ('تنیس', 'تنیس'),
        ('بسکتبال', 'بسکتبال'),
        ('والیبال', 'والیبال'),
        ('پینتبال', 'پینتبال'),
        ('بازی های کامپیوتری', 'بازی های کامپیوتری'),
        ('شطرنج', 'شطرنج'),
        ('دیگر', 'دیگر'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        null=True, upload_to=get_upload_path, blank=True)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=20, null=True)
    tell=models.CharField(max_length=12,null=True,blank=True)
    email=models.EmailField(max_length=80,null=True,blank=True)
    favorite=MultiSelectField(max_length=200,null=True,choices=fav_list,blank=True)
    orgin_fav=models.CharField(max_length=20,null=True,blank=True,choices=fav_list)
    gender = models.CharField(max_length=11,null=True, choices=gender_list)
    city = models.CharField(max_length=10, null=True, blank=True ,choices=city_list)
    birth_date = jmodels.jDateField(null=True ,blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    code=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username

    def avatar_url(self):
        return self.avatar.url if self.avatar else 'http://127.0.0.1:8000/static/app_profile/img/avatar.png'
    def profile_url(self):
        return reverse('profile',args=(self.user.username,))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# Create your models here.



 
class Contact(models.Model):
    name=models.CharField(max_length=30,null=True)
    title=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(null=True)
    tell=models.CharField(max_length=14,null=True,blank=True)
    messages=models.CharField(null=True,max_length=400)


    class Meta:
        verbose_name_plural=('تماس با ما')

    def __str__(self):
        return self.name+'_'+self.title


class Fav(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)


    class Meta:
       verbose_name_plural=('پینهاد به کاربر')

    



    

    def fav(self):
       if self.user.profile.favorite in  self.event.Event_type :
         return self.event.Event_type
