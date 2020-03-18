from django.shortcuts import render, get_object_or_404

from .models import Blogs

def allblogs(request):
    blogs = Blogs.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail })
        
