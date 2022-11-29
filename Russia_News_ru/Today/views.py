from django.shortcuts import render
from .models import Posts, Comments
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your views here.

# ГЛАВНАЯ
def index(request):
     return render(request, 'home.html')

# О НАС
def profile(request):
    return render(request, 'profile.html')

# НОВОСТИ
def posts(request):
     posts = Posts.objects.all()
     return render(request, 'posts.html', {'posts': posts})

# ФОРУМ
def forum(request):
     posts = Comments.objects.all()
     return render(request, 'forum.html', {'posts': posts})
     

# Новый комментарий c картинкой или смайликом
def newpost(request):
     title = request.POST.get('title')
     text = request.POST.get('text')
     file = request.FILES['file']
     fss = FileSystemStorage('Today/static/images/')
     saved_file = fss.save(file.name, file)
     post = Comments()
     post.title = title
     post.text = text
     post.image = file.name
     post.save()
     return HttpResponseRedirect('/forum')

