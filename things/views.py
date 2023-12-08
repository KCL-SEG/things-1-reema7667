from django.shortcuts import render

# Create your views here.

def home(request):
    """Display the current user's home."""
    return render(request, 'home.html')