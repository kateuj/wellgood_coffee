from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def custom_404(request, exception=None):
    """
    Render custom 404 error template
    """
    return render(request, '404.html', status=404)