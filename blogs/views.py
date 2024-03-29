from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from.forms import BlogForm

def check_user_post(request, post):
    """Check if the user wanting to edit the post is associated with it"""
    if post.owner != request.user:
        raise Http404

# Create your views here.
def blog(request):
    """The home page for the blog posted"""
    blogposted = BlogPost.objects.order_by('-date_added')
    
    context = {'blogposted': blogposted}
    return render(request, 'blogs/home.html', context)

# Want to make sure the user is logged in before edit/add blog post.
@login_required
def edit_blog(request, blog_id): 
    """Edit the blog posted """
    blogpost = BlogPost.objects.get(id=blog_id)
    check_user_post(request, blogpost)
    
    if request.method != 'POST':
        form = BlogForm(instance=blogpost)        
    else:
        form = BlogForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')
        
    # Display a blank format
    # Should pass blog to the template in your view. Since you're editing a specific blog post, you should pass the blogpost variable to the template instead.
    context = {'form': form, 'blogpost': blogpost}
    return render(request, 'blogs/edit_blog.html', context) # Then in your edit_blog.html template, use blogpost.id instead of blog.id

# Want to make sure the user is logged in before edit/add blog post.       
@login_required
def add_blog(request):
    """Adding a new blog post"""
    # Do not need Blog ID because adding a new one that does not exist yet
    if request.method != 'POST':
        # Creating a blank form
        form = BlogForm()
    else: 
        form = BlogForm(data=request.POST)
        if form.is_valid():
            # Need to associate the user with the new post
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            
            return redirect('blogs:blog')
    
    # Returning a blank form if not valid or error
    context = {'form': form}
    return render(request, 'blogs/add_blog.html', context)