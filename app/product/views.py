from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView
from product.models import Product
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from product.forms_p import Product_form_for_create

class HomeView(TemplateView):
    template_name = "home.html"


class CreateProductView(CreateView):
    template_name = "create.html"
    model = Product
    form_class = Product_form_for_create
    success_url = reverse_lazy("home-link")


class ProductListView(ListView):
    template_name = "product_list.html"
    model = Product


class ProductDetailsView(DetailView):
    template_name = "details.html"
    model = Product


class ProductUpdateView(UpdateView):
    template_name = "update.html"
    model = Product
    fields = ('name_product', 'price', 'description')
    success_url = reverse_lazy("home-link")


class ProductDeleteView(DeleteView):
    template_name = "delete.html"
    model = Product
    success_url = reverse_lazy("home-link")
