from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Coffe, Publication, Comment, Contacts, ClientContact

from django.shortcuts import render, redirect
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all(),
            'comment_list': Comment.objects.all(),
            'blog': Publication.objects.all(),
            'contacts': Contacts.objects.first()
        }
        return context






class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffe_list': Coffe.objects.all(),
            'contacts': Contacts.objects.all()
        }
        return context


class CoffeeView(TemplateView):
    template_name = 'coffee.html'


# class BlogView(TemplateView):
#     template_name = 'blog.html'
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'blog': Publication.objects.all()
#         }
#         return context

def blog_view(request):
    context = {
        'blog': Publication.objects.all(),
        'contacts': Contacts.objects.all()
    }
    response = render(request, 'index.html', context)
    return response



class CoffeDetail(TemplateView):
    coffee_pk = 'coffe.html'
    def get_context_data(self, **kwargs):
        coffee_pk = kwargs['pk']

        context = {
            'coffee': Coffe.object.get(id=coffee_pk)
        }
        return context


class DetailCoffeeView(TemplateView):
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        coffe_pk = kwargs['pk']
        context = {
         'coffee': Publication.objects.get(id=coffe_pk)
        }
        return context





def visitor_message_view(request):
    print('это ваш данные от ПОСТ запроса', request.POST)

    input_name = request.POST['Your Name']
    input_email = request.POST['Your Email']
    input_phone = request.POST['Your Phone']
    input_message = request.POST['Massage']

    ClientContact.objects.create(name=input_name, email=input_email, phone=input_phone, message=input_message)

    return HttpResponse("<h1>Ваше сообщение было создано!</h1>")
