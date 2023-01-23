from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fun, name='fun'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.services, name='service'),
    path('package', views.package, name="package"),
    path('trip', views.trip, name="trip"),
]
