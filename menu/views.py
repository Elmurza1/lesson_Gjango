from django.views.generic import TemplateView
from .models import Coffe
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all()
        }
        return context

class CoffeesView(TemplateView):
    template_name = 'coffee.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all()
        }
        return context

class CoffeeView(TemplateView):
    template_name = 'coffe.html'

class BlogView(TemplateView):
    template_name = 'blog.html'
