import email
from email import message
from django.db.models import Q
from turtle import title
from django.shortcuts import get_object_or_404 , render , redirect
from .models import Post ,Category
from .forms import CommentForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    post = Post.objects.filter(status= Post.ACTIVE)
    return render(request, 'index.html',{'posts':post})

def base(request):
    return render(request, 'base.html')

def detail(request, slug):
    post = get_object_or_404(Post , slug=slug ,status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'posts':post, 'form':form })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'category.html' ,{'category':category , 'posts':posts})

def search(request):
    query = request.GET.get('query','')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'search.html', {'posts':posts ,'query':query})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # send_mail(name, message, settings.EMAIL_HOST_USER,[email],fail_silently=False)
        mail=send_mail(name, message, email, ['kokominhein96@gmail.com'])
        mail.fail_silently = True
        mail.send()


        return render(request, 'index.html',{'name':name})

    else:
        return render(request,'index.html')
