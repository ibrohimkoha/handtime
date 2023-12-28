from django.urls import path
from .views import index, about , contact, testimonial, product
app_name = 'pages'
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('testimonial/', testimonial, name='testimonial'),
    path('product/', product, name='product'),
]