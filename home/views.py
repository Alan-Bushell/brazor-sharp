from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


def handle_404_error(request, exception):
    """View to return 404 if page not found"""
    template = 'home/templates/home/404.html'
    return render(request, template, {})


def handle_500_error(request):
    """View to return 500 if page not found"""
    template = 'home/templates/home/500.html'
    return render(request, template, {})
