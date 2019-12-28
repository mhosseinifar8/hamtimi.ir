from django.shortcuts import render, get_object_or_404
from app_event.models import Event,Answer,Support,messages as me
from app_blog.models import Blog,Landing,Comment
from app_reserve.models import Reserve
from app_event.forms import Add_event
from app_profile.models import Profile,Fav
from django.shortcuts import redirect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from app_event.forms import ConfirmForm
from app_event.models import Confrim
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
import jdatetime
import random
import requests

def event_func(request):
  event = Event.objects.all()
  
  if request.method=='POST':
     name=request.POST.get('name')
     cat=Event.objects.filter(name)
     return render(request,'event.html',{'cat':cat})

  else:
    return render(request, 'event.html', {'event': event})
        



  
@login_required
def message(request,pk):
    event=get_object_or_404(Event,pk=pk)
    mess=me.objects.all()
    if request.method=="POST":
        sender=request.user
        ev=event
        message=request.POST.get("message")
        inbox=me()
        inbox.sender=sender
        inbox.resiver=ev
        inbox.message=message
       
        inbox.save()
        return redirect('chat',pk=event.pk)
    else:
      return redirect('home')



def home(request):
    blog=Blog.objects.order_by('-time')[0:3]
    salon=Reserve.objects.order_by('-datetime')[0:6]
    landing=Landing.objects.all()
    if request.method=='GET':
       query=request.GET.get('q')
       query2=request.GET.get('n')
       query3=request.GET.get('t')
       if query2 is not None :
          req=Q(saloon_name__icontains=query)|Q(event_name__icontains=query)
          req2=Q(City__icontains=query2)
          req3=Q(Event_type__icontains=query3) 
          result=Event.objects.filter(req,req2,req3).distinct()
          return render(request,'index.html',{'result':result,'blog':blog,'landing':landing})
       else:
           return render(request,'index.html',{'blog':blog,'landing':landing,'salon':salon})
    else:
       return render(request,'index.html',{'blog':blog,'landing':landing,'salon':salon})  
    return render(request, 'index.html',{'blog':blog,'landing':landing,'salon':salon})


def event_cat(request):
      if request.method=='GET':
          event=Event.objects.all()
          query=request.GET.get('type')
          req=Q(Event_type__icontains=query)
          result=Event.objects.filter(req).distinct()
          return render(request,'event-cat.html',{'result':result})
      else:
       return render(request,'event-cat.html')    
          


def landing(request,slug):
  landing=Landing.objects.all()
  return render(request,'landing.html',{'landing':landing})

@login_required
def dashboard(request):
  
  req2=Profile.objects.all()
  req=Confrim.objects.all()
  event=Event.objects.all()
 
 


  return render(request,'dashboard.html',{'event':event,'req':req,'req2':req2})

@login_required
def waiting(request):
   eventt=Event.objects.all()
   return render(request,'dashboard-my-event-waiting.html',{'eventt':eventt})  


def not_find(request):
  return render(request, '404.html')

@login_required
def new_event(request):
  return render(request,'dashboard-add-event.html')

@login_required
def new(request):
  if request.method == 'POST':
    creator=request.user
    salon_name=request.POST.get('salon_name')
    event_name=request.POST.get('event_name')
    Event_type=request.POST.get('event_type')
    gender=request.POST.get('gender')
    state=request.POST.get('state')
    City=request.POST.get('city')
    address=request.POST.get('address')
    date=request.POST.get('date')
    time=request.POST.get('time')
    period_of_time=request.POST.get('period')
    des=request.POST.get('des')
   
    total=request.POST.get('total')
    needed=request.POST.get('needed')
    total_cost=request.POST.get('total_cost')
    event=Event()
    event.creator=creator
    event.saloon_name=salon_name
    event.event_name=event_name
    event.Event_type=Event_type
    event.gender=gender
    event.address=address
    event.City=City
    event.state=state
    event.date=date
    event.time=time
    event.period_of_time=period_of_time
    event.Description=des
    
    event.total=total
    event.total_cost=total_cost
    event.needed=needed
    event.save()
    messages.success(request,'رویداد شما با موفقیت ایجاد شد')
    return redirect('my_events')
  else:
    return redirect('new_event')



@login_required
def edit(request,pk):
  event = get_object_or_404(Event, pk=pk)
  if request.method == 'POST':
    creator=request.user
    salon_name=request.POST.get('salon_name')
    event_name=request.POST.get('event_name')
    Event_type=request.POST.get('event_type')
    gender=request.POST.get('gender')
    state=request.POST.get('state')
    City=request.POST.get('city')
    address=request.POST.get('address')
    date=request.POST.get('date')
    time=request.POST.get('time')
    period_of_time=request.POST.get('period')
    des=request.POST.get('des')
   
    total=request.POST.get('total')
    needed=request.POST.get('needed')
    total_cost=request.POST.get('total_cost')
    eventt=Event()
    eventt=event
    eventt.creator=creator
    eventt.saloon_name=salon_name
    eventt.event_name=event_name
    eventt.Event_type=Event_type
    eventt.gender=gender
    eventt.address=address
    eventt.City=City
    eventt.state=state
    eventt.date=date
    eventt.time=time
    eventt.period_of_time=period_of_time
    eventt.Description=des
    
    eventt.total=total
    eventt.total_cost=total_cost
    eventt.needed=needed
    eventt.save()
    messages.success(request,'رویداد شما با موفقیت ایجاد شد')
    return redirect('my_events')
  else:
    return render(request,'event-edit.html',{'event':event})


def event_edit(request,pk):
   event=get_object_or_404(Event,pk=pk)
   return render(request,'event-edit.html',{'event':event})          
      
        
    

def event_detail(request, pk):
  try:
    mess=me.objects.all()
    detail = Event.objects.get(pk=pk)
  except (ObjectDoesNotExist,PageNotAnInteger,EmptyPage):
    return redirect('home')
  return render(request, 'event-detail2.html', {'detail':detail,'mess':mess})


@login_required
def chat_room(request,pk):
  event=get_object_or_404(Event,pk=pk)
  detail = Event.objects.get(pk=pk)
  return render(request,'dashboard-messages-conversation.html',{'detail':detail,'event':event})


@login_required
def inbox(request):
  event=Confrim.objects.all()
  con=Event.objects.all()
  return render(request,'dashboard-messages.html',{'event':event,'con':con})



@login_required
def remove_event(request,pk):
   
   eventt=get_object_or_404(Event,pk=pk)
   if request.user==request.POST.get('created'):
       event=get_object_or_404(Event,pk=pk)
       event.delete()
       return redirect('not_find')
   else:
       return redirect('event_detail',pk=eventt.pk)


def delete_event_time(request,pk):
   event=get_object_or_404(Event,pk=pk)
   now=jdatetime.datetime.now()
   if event.date.month < now.month:
      return event.delete()
   else:
      return


@login_required          
def my_events(request):
  event=Event.objects.all()
  return render(request,'dashboard-my-events.html',{'event':event})







@login_required
def expire(request):
   event=Event.objects.all()
   return render(request,'dashboard-my-events-expire.html',{'event':event})



@login_required
def confrim_event(request,pk):
  e= get_object_or_404(Event, pk=pk)  
  if request.method=='POST':
        form=ConfirmForm(request.POST)
        if form.is_valid():
          confrim=form.save(commit=False)
          confrim.e=e
          confrim.user=request.user
          confrim.event=e
          confrim.save()
          return render(request,'confirmation.html')
  

  else:
    form=ConfirmForm()
  return render(request,'confrim.html',{'form':form,'e':e})  


@login_required
def user_list(request,pk):
     user_request=get_object_or_404(Event,pk=pk)
     return render(request,'user-list.html',{'user_request':user_request})



@login_required
def approve(request,pk):
      user_req=get_object_or_404(Confrim,pk=pk)
      if user_req.event.creator==request.user:
          user_req.approve()
          return HttpResponse('<h1>Done</h1>')
      else:
        return HttpResponse('<h1>sry</h1>')    

   
@login_required
def delete_approve(request,pk):
      user_req=get_object_or_404(Confrim,pk=pk)
      if user_req.event.creator==request.user:
          user_req.delete()
          return HttpResponse('<h1>Done</h1>')
      else:
        return HttpResponse('<h1>sry</h1>')   


def search_event(request):
  if request.method=='GET':
    query=request.GET.get('q')
    query2=request.GET.get('n')
    query3=request.GET.get('t')
    if query2 is not None :
      req=Q(saloon_name__icontains=query)|Q(event_name__icontains=query)
      req2=Q(City__icontains=query2)
      req3=Q(Event_type__icontains=query3) 
      result=Event.objects.filter(req,req2,req3).distinct()

      return render(request,'search.html',{'result':result})
    else:
      return render(request,'search.html')
  else:
    return render(request,'search.html')  


def search_salon(request):
        salon_name='انقلاب'
        url = 'https://api.neshan.org/v1/search?term={salon_name}&lat=35.83266&lng=50.99155'.format(
            salon_name=salon_name)
        header = {
            'Api-Key': ''
        }
        resspon = requests.get(url, headers=header)

        t = resspon.json()['items']
        
        return render(request,'tt.html',{'t':t})        
         



def search_blog(request):
  if request.method=='GET':
    query=request.GET.get('s')
    if query is not None:
      req=Q(title__icontains=query)|Q(content__icontains=query)
      result=Blog.objects.filter(req).distinct()
      return render(request,'search2.html',{'result':result})
    else:
      return render(request,'search2.html',{'result':result})
  else:
    return redirect('blog')    
         


def about_us(request):
  return render(request,'about.html')


def privacy(request):
  return render(request,'privacy.html')

@login_required
def support(request):

   if request.method=='POST':
    
      
      user=request.user
      title=request.POST.get('title')
      message=request.POST.get('message')
      block=request.POST.get('block')
      sup=Support()
      sup.user=user
      sup.title=title
      sup.message=message
      sup.block=block
      
      sup.save()
      return redirect('tickets' , pk=sup.pk )
   else:
     return redirect('home')  

@login_required
def answer(request):
  return render(request,'ticket.html')

@login_required
def all_ticket(request):
  ticket=Support.objects.all()
  return render(request,'all_ticket.html',{'ticket':ticket})
@login_required
def tickets(request,pk):
  tic=Support.objects.all()
  ans=Answer.objects.all()

  ticket=get_object_or_404(Support,pk=pk)
  return render(request,'tickets.html',{'ticket':ticket,'tic':tic,'ans':ans})