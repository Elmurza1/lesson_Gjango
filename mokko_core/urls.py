from django.contrib import admin
from django.urls import path
from menu.views import HomeView, blog_view, CoffeeView, CoffeesView, CoffeDetail, DetailCoffeeView, visitor_message_view
from django.conf.urls.static import static
from django.conf.urls.static import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-list'),
    path('coffees/', CoffeesView.as_view(), name='coffe-list'),
    path('coffee/', CoffeeView.as_view()),
    path('blog/', blog_view, name='blog-list'),
    path('coffee/<int:pk>/', CoffeDetail.as_view(), name='coffe_detail_url'),
    path('detail/<int:pk>', DetailCoffeeView.as_view()),
    path('home/client-contact-create/', visitor_message_view)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
