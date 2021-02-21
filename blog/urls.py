from django.urls import path
from .views import post_list,PostCreateView,PostUpdateView,PostDeleteView,post_detail,upvote_post


urlpatterns=[
	path('',post_list,name='blog-home'),
	path('post/new/',PostCreateView.as_view(),name='post-create'),
	path('post/<int:pk>/',post_detail,name='post-detail'),
	path('post/upvote/',upvote_post,name='upvote_post'),
	path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]
