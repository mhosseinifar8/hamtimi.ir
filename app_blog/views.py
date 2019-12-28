from django.shortcuts import render, get_object_or_404
from app_blog.models import Blog,Comment,REP_CM
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator


def blog(request):
  post=Blog.objects.all()
  pagination=Paginator(post,5)
  page=request.GET.get('page')
  blog=pagination.get_page(page)

  return render(request,'pages-blog.html',{'blog':blog})




def blog_post(request,title):
	comment=Comment.objects.all()
	rep=REP_CM.objects.all()
	blog=get_object_or_404(Blog,title=title)
	return render(request,'pages-blog-post.html',{'blog':blog,'comment':comment,'rep':rep})

	

@login_required
def comment(request,title):
  e=get_object_or_404(Blog,title=title)
  if request.method == 'POST':
    user=request.user
    comm=request.POST.get('com')
    bblog=e
    replay_comment=request.POST.get('rep')
    add_comment=Comment()
    add_comment.user=user
    add_comment.replay_comment="0"
    add_comment.comment=comm
    add_comment.blog=bblog
    add_comment.save()
    return redirect('post',title=e.title)
  else:
   return redirect('home') 

@login_required
def rep_comment(request,title):
  e=get_object_or_404(Blog,title=title)
  if request.method == 'POST':
    user=request.user
    bblog=e
    comm=request.POST.get('com')
    rep_comment=request.POST.get('reply')
    add_comment=REP_CM()
    add_comment.user=user
   # add_comment.rep=rep_comment
    add_comment.blog=bblog
    add_comment.comment=comm
    add_comment.save()
    return redirect('post',title=e.title)
  else:
   return redirect('home') 
   


# Create your views here.
