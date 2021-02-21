from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
            ListView,
            CreateView,
            UpdateView,
            DeleteView,
            )
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from users.models import Profile


# Create your views here.
def post_list(request):
	post_list=Post.objects.all()
    # post_temp=Post.objects.filter(user__username=user)
    # post_count = post_temp.count()

	context={'posts':post_list}
	return render(request,'blog/home.html',context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','description','city','img','location']
    # fields=['location','name']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have created a new post!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','description','city','img','location']

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have edited your post!')
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/blog"
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    is_upvoted=False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted=True
    if request.method=="POST":
        return HttpResponseRedirect(reverse('post-detail',args=(pk,)))
    context={
        'post':post,
        'is_upvoted': is_upvoted,
        'total_upvotes':post.total_upvotes(),
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def upvote_post(request):
    pk=request.POST.get('post_id')
    post=get_object_or_404(Post,id=pk)
    is_upvoted=False
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted=False
    else:
        post.upvotes.add(request.user)
        is_upvoted=True
        request.user.profile.reputation+=1
        request.user.save()
        if(request.user.profile.reputation>15):
            request.user.is_verified=True
    return HttpResponseRedirect(reverse('post-detail', args=(pk, )))


