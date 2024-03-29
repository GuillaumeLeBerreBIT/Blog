from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """A blog post the user writes about"""
    
    title = models.CharField(max_length=200) # Title for the post
    text = models.TextField() # The event to write about    
    date_added = models.DateTimeField(auto_now_add=True) # Adding the date 
    # Associate the blogpost with each user (upon deleting all posts with associated user deleted)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the blog post title"""
        if len(self.title) > 50:
            return f"{self.title[:50]} ..."
        else:
            return f"{self.title}"
    