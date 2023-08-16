from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import TouristPlace, PaymentItem
from account.forms import CarForm


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class DestinationView(TemplateView):
    template_name = 'destination.html'


class GuideView(TemplateView):
    template_name = 'guide.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class PackageView(TemplateView):
    template_name = 'package.html'


class ServiceView(TemplateView):
    template_name = 'service.html'


class TestimonialView(TemplateView):
    template_name = 'testimonial.html'


@user_passes_test(lambda user: user.is_superuser)
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('my_products')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = CarForm()
    return render(request, 'add_product.html', {'form': form})

class CarView(TemplateView):
    template_name = 'car.html'

def search_results_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = TouristPlace.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)


@login_required(login_url='login/')        #отображение на корзинке
def profile_view(request):
    myitems = TouristPlace.objects.all().values()

    template = loader.get_template('payment.html')    #обрати внимание на payment.html
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))


@login_required
def payment_views(request):
    user = request.user

    payment_items = PaymentItem.objects.filter(user=user)

    context = {'payment_items': payment_items}
    return render(request, 'payment.html', context)


@login_required                                             #remove из корзинки
def remove_from_basket(request, item_id):
    user = request.user
    item = get_object_or_404(TouristPlace, pk=item_id)

    try:
        basket_item = PaymentItem.objects.get(user=user, product=item)
        basket_item.delete()
    except PaymentItem.DoesNotExist:
        pass

    return redirect('basket')


def calculate_subtotal(products_in_cart):     #для цен
    subtotal = 0
    for product in products_in_cart:
        subtotal += product.price
    return subtotal


def summ_views(request):
    session = Session.objects.get(session_key=request.session.session_key)
    products_in_cart = session.get('products_in_cart', [])

    subtotal = calculate_subtotal(products_in_cart)

    total = subtotal
    print(total)
    print(subtotal)                                                                    #общая сумма
    context = {
        'products_in_cart': products_in_cart,
        'subtotal': subtotal,
        'total': total
    }

    return render(request, 'basket.html', context)


