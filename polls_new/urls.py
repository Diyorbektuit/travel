from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('destination/', views.DestinationView.as_view(), name='destination'),
    path('guide/', views.GuideView.as_view(), name='guide'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('package/', views.PackageView.as_view(), name='package'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('single/', views.SingleView.as_view(), name='single'),
    path('testimonial/', views.TestimonialView.as_view(), name='testimonial'),
]

