from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    blogs_list = BlogModel.objects.all()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(blogs_list, 4)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs
    }
    return render(request, 'home/home.html', context)

@login_required
def blog_detail(request, slug):
    context = {
        'blog': BlogModel.objects.filter(slug=slug).first()
    }
    return render(request, 'home/blog_detail.html', context)

def user_blogs(request):
    context = {
        'blogs': BlogModel.objects.filter(user=request.user).all()
    }
    return render(request, 'home/user_blogs_list.html', context)

def blog_delete(request, id):
    blog_obj = BlogModel.objects.get(id = id)
    if blog_obj.user == request.user:
        blog_obj.delete()
    return redirect(request.META['HTTP_REFERER'])

def blog_update(request, slug):
    blog_obj = BlogModel.objects.get(slug =slug)
    if not blog_obj.user == request.user:
        return redirect('/')
    initial_dict = {'content': blog_obj.content}
    form = BlogForm(initial=initial_dict)
    context = {
        'blog': blog_obj,
        'form': form
    }
    if request.method=="POST":
        form = BlogForm(request.POST)
        image = request.FILES['image']
        title = request.POST.get('title')
        user = request.user
        if form.is_valid():
            content = form.cleaned_data['content']
        BlogModel.objects.create(
            user = user, 
            title=title,
            content = content,
            image = image 
        )
        return redirect('home')
    return render(request, 'home/update_blog.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home/register.html')

def add_blog(request):
    context = {
        'form': BlogForm
    }
    if request.method=="POST":
        form = BlogForm(request.POST)
        image = request.FILES['image']
        title = request.POST.get('title')
        user = request.user
        if form.is_valid():
            content = form.cleaned_data['content']
        BlogModel.objects.create(
            user = user, 
            title=title,
            content = content,
            image = image 
        )
        return redirect('home')
    return render(request, 'home/add_blog.html', context=context)