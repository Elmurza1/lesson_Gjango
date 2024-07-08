from django.views.generic import TemplateView
from .models import Coffe, Publication
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all()
        }
        return context


class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all()
        }
        return context


class CoffeeView(TemplateView):
    template_name = 'coffee.html'


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = {
            'blog': Publication.objects.all()
        }
        return context

class CoffeDetail(TemplateView):
    coffee_pk = 'coffe.html'
    def get_context_data(self, **kwargs):
        coffee_pk = kwargs['pk']

        context = {
            'coffee': Coffe.object.get(id=coffee_pk)
        }
        return context


class PublicationDetailView(TemplateView):
    pass

