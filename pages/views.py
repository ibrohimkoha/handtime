from django.shortcuts import render
from .models import WatchModel
# Create your views here.

def index(request):
    topsale = WatchModel.objects.filter(category__name__icontains='top')
    feature = WatchModel.objects.filter(category__name__icontains='feature')
    new = WatchModel.objects.filter(category__name__icontains='new')

    context = {
        'topsale': topsale,
        'feature': feature,
        'new': new
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def product(request):
        topsale = WatchModel.objects.filter(category__name__icontains='top')
    feature = WatchModel.objects.filter(category__name__icontains='feature')
    new = WatchModel.objects.filter(category__name__icontains='new')

    context = {
        'topsale': topsale,
        'feature': feature,
        'new': new
    }
    return render(request, 'product.html', conext=context)

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
