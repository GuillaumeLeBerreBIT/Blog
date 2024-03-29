"""Define the URL patterns for Blogs"""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    # Make sure the name is the same as the name called in the urls, it matches the name not the function name!
    path('', views.blog, name='blog'),
    # Edit the blog post
    # Here it will take the variable and send the ID to the function to process correct post
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    # Adding a new blog post
    path('add_blog/', views.add_blog, name='add_blog'),
]