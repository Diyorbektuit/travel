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
    path('testimonial/', views.TestimonialView.as_view(), name='testimonial'),
    path('remove/<int:product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('search/', views.search_results_view, name='search_results'),
    path('add/', views.add_car, name='add_car'),
    #path('summ_views/<int:product_id>/', views.summ_views, name='summ_views'),
    path('car/', views.CarView.as_view(), name='car'),

]

