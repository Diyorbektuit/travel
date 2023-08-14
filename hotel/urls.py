from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hotels/', views.hotel_list, name="hotels"),
    path('hotels/<int:pk>/', views.hotel_detail, name="hotel")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

