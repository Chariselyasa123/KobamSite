from django.shortcuts import render
from .models import Post 

# Create your views here.

def about(request):
    return render(request, 'blog/base.html')

def materi(request):

    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/materi.html', context)