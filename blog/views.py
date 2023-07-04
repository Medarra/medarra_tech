# blog/views.py
from django.shortcuts import render
from django.db.models import Count
from . import models


def home(request):
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    popular_topics = models.Topic.objects.all().annotate(posts_count=Count('blog_posts'))[:5]
    # Add as context variable "latest_posts"
    context = {
        'latest_posts': latest_posts,
        'popular_topics': popular_topics}
    return render(request, 'blog/home.html', context)
