from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('add-blog/', add_blog, name='add_blog'),
    path('blog-detail/<slug>/', blog_detail, name='blog_detail'),
    path('user-blogs/', user_blogs, name='user_blogs'),
    path('blog-update/<slug>/', blog_update, name='blog_update'),
    path('blog-delete/<id>/', blog_delete, name='blog_delete'),
    path('logout/', logout_view, name='logout')
]