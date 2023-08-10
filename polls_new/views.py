from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView


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


class SingleView(TemplateView):
    template_name = 'single.html'


class TestimonialView(TemplateView):
    template_name = 'testimonial.html'


