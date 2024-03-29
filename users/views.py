from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Registering a new user."""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else: 
        # Process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            # Want to save the new user into the database
            new_user = form.save()
            # Want to directly login the new user
            login(request, new_user)
            # Send back to the home page
            return redirect('blogs:blog')
    
    # Returning a blank form
    context = {'form': form}
    return render(request, 'registration/register.html', context)