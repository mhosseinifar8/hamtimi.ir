from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation,GenericForeignKey
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse


def blog_image(instance,filename):
	return 'image/{title}/{filename}'.format(
		title=instance.title,
		filename=filename
		)

class Blog(models.Model):
	author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	create_time=jmodels.jDateField(auto_now_add=True,null=True)
	time=models.DateTimeField(auto_now_add=True,null=True)
	descript=models.CharField(max_length=200,null=True,blank=True)
	title=models.CharField(max_length=100,null=True,blank=True)
	content=FroalaField(theme='dark')
	image=models.ImageField(null=True,upload_to=blog_image,blank=True)
	cat=models.CharField(max_length=20,null=True,blank=True)


   


	def get_absolute_url(self):
		return reverse('post',args=(self.title,))

	
	def __str__(self):
	    return self.title	




def landing_img(instance,filename):
	return 'landing_img/{title}/{filename}'.format(
         title=instance.title,
         filename=filename

		)


class Landing(models.Model):
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=50,null=True)
    descript=models.CharField(max_length=80,null=True)
    create_time=jmodels.jDateField(auto_now_add=True,null=True)
    content=FroalaField(theme='dark')
    slug=models.SlugField(max_length=40)
    image=models.ImageField(null=True,upload_to=landing_img)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
       return reverse('landing',args=(self.slug,))	
# Create your models here.



class Comment(models.Model):
	class Meta:
		verbose_name_plural='کامنت'

	user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	replay_comment=models.CharField(null=True,max_length=100)
	blog=models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True,related_name='comments')
	comment=models.CharField(max_length=90,null=True)
	create_time=jmodels.jDateField(auto_now_add=True,null=True)


	def __str__(self):
		return self.user.username 

	
	def cm_url(self):
	  return reverse('comment',args(self.pk,))	



class REP_CM(models.Model):
     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     comment=models.CharField(max_length=100,null=True)
     rep=models.ForeignKey(Comment,on_delete=models.SET_NULL,null=True,related_name='rep')
     blog=models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
     create_time=jmodels.jDateField(auto_now_add=True,null=True)


     def __str__(self):
       return self.user.username + self.comment   
  



