from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

from .models import BlogPost
from.forms import BlogForm

def check_user_post(request, post):
    """Check if the user wanting to edit the post is associated with it"""
    if post.owner != request.user:
        raise Http404

# CREATE YOUR VIEWS HERE.
def index(request):
    """The home page of the blog site"""
    return render(request, 'blogs/index.html')

@login_required
def blog(request):
    """Page containing the blog posts"""
    blogposted = BlogPost.objects.order_by('-date_added')
    
    context = {'blogposted': blogposted}
    return render(request, 'blogs/home.html', context)

# Want to make sure the user is logged in before edit/add blog post.
@login_required
def edit_blog(request, blog_id): 
    """Edit the blog posted """
    #blogpost = BlogPost.objects.get(id=blog_id)
    blogpost = get_object_or_404(BlogPost, id=blog_id)
    # Check if the user requested to edit owns the post.
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

# Want to make it so the user can delete his own posts
@login_required
def delete_post(request, blog_id):
    """Deleting a Post"""
    blogpost = get_object_or_404(BlogPost, id=blog_id)
    # Need to check if the request by the user is of his own post.
    check_user_post(request, blogpost)
    
    context = {'post': blogpost}
    # View a page to make sure the user wants to delete the post
    if request.method == 'GET':
        return render(request, 'blogs/post_confirm_delete.html', context)
    
    elif request.method =='POST':
        # Delete the POST
        blogpost.delete()
        # Create a flash message and redirect the user to the blog posts page.
        #messages.success(request, 'The post has been deleted successfully!')
        return redirect('blogs:blog')

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