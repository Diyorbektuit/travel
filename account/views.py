from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/add_car/')
            else:
                login(request, user)
                return redirect('/')
        else:
            return render(request, self.template_name, {'error': 'Неверные учетные данные'})

        return super().post(request, *args, **kwargs)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and request.user.is_superuser:
    #         return super().get(request, *args, **kwargs)
    #     return redirect('/')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        return redirect('login')


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser, login_url='index')
def admin_action(request):
    return render(request, 'add_car.html')
