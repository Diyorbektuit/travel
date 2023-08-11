from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Шаблон для страницы входа

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template_name, {'error': 'Неверные учетные данные'})

        return super().post(request, *args, **kwargs)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')