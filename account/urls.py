from django.urls import path
from polls_new import views
from .views import CustomLoginView, CustomRegisterView


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('profile', views.profile_view, name='profile'),

]