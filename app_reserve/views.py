from django.shortcuts import render,get_object_or_404
from app_reserve.models import Reserve,Comment_Salon
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import Q

def saloon(request):
  saloon=Reserve.objects.all()
  pagination=Paginator(saloon,9)
  page=request.GET.get('page')
  salon=pagination.get_page(page)
  if request.method == 'GET':
    query=request.GET.get('n')
    query2=request.GET.get('c')
    query3=request.GET.get('l')
    if query2 is not None:
      req=Q(salon_name__icontains=query)|Q(salon_type__icontains=query)|Q(salon_sport__icontains=query)
      req2=Q(city__icontains=query2)
      req3=Q(salon_type__icontains=query3)
      res=Reserve.objects.filter(req,req2,req3).distinct()
      pagination=Paginator(res,9)
      page=request.GET.get('page')
      result=pagination.get_page(page)

      return render(request,'all-saloon.html',{'result':result})
    else:
      return render(request,'all-saloon.html',{'salon':salon})  
  else:
    return render(request,'all-saloon.html',{'salon':salon})

def salon_detail(request,salon_name):
  salon=Reserve.objects.get(salon_name=salon_name)
  return render(request,'salon-detail.html',{'salon':salon})



def cm_salon(request,salon_name):
	comment=get_object_or_404(Reserve,salon_name=salon_name)
	if request.method == 'POST':
		user=request.POST.get('first_name')
		email=request.POST.get('email')
		message=request.POST.get('message')
		salon=comment
		star=request.POST.get('star')
		add_comment=Comment_Salon()
		add_comment.user=user
		add_comment.message=message
		add_comment.salon=salon
		add_comment.email=email
		add_comment.star=star
		add_comment.save()
		return redirect('salon_detail' ,salon_name=comment.salon_name)
	else:
	 return redirect('home')	