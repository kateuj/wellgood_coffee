from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/send/', views.contact_send, name='contact_send'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
