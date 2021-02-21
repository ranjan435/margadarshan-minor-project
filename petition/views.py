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
def petition_list(request):
	petition_list=Petition.objects.all()
    # post_temp=Post.objects.filter(user__username=user)
    # post_count = post_temp.count()

	context={'petition':petition_list}
	return render(request,'petition/home.html',context)

class PetitionCreateView(LoginRequiredMixin,CreateView):
    model=Petition
    fields=['title','description','city','img','location']
    # fields=['location','name']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have created a new post!')
        return super().form_valid(form)

class PetitionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Petition
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

class PetitionDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/petition"
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

def petition_detail(request,pk):
    petition=Petition.objects.get(id=pk)
    is_upvoted=False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted=True
    if request.method=="POST":
        return HttpResponseRedirect(reverse('petition-detail',args=(pk,)))
    context={
        'petition':petition,
        'is_upvoted': is_upvoted,
        'total_upvotes':petition.total_upvotes(),
    }
    return render(request,'petition/petition_detail.html',context)

@login_required
def upvote_petition(request):
    pk=request.POST.get('petition_id')
    petition=get_object_or_404(Petition,id=pk)
    is_upvoted=False
    if petition.upvotes.filter(id=request.user.id).exists():
        petition.upvotes.remove(request.user)
        is_upvoted=False
    else:
        petition.upvotes.add(request.user)
        is_upvoted=True
    return HttpResponseRedirect(reverse('petition-detail', args=(pk, )))


