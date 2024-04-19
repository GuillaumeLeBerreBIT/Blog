"""Define the URL patterns for Blogs"""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Blog posts
    # Make sure the name is the same as the name called in the urls, it matches the name not the function name!
    path('blogs/', views.blog, name='blog'),
    # Edit the blog post
    # Here it will take the variable and send the ID to the function to process correct post
    path('blogs/edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    # Adding a new blog post
    path('blogs/add_blog/', views.add_blog, name='add_blog'),
    # Deleting a post created
    path('blogs/delete_post/<int:blog_id>/', views.delete_post, name='delete_post'),
]