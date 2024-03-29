"""Define the URL patterns for the user"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Including the default authorisation URLs.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]