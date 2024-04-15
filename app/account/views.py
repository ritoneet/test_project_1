from django.urls import reverse

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from account.Reg_form import Reg_form_class
from django.shortcuts import get_object_or_404

class MyPageView(UpdateView):
    template_name = "update.html"
    queryset = User.objects.all()
    fields = ('username', 'email', 'date_joined')
    success_url = reverse_lazy("home-link")


class RegPageView(CreateView):
    template_name = "registration.html"
    model = User
    form_class = Reg_form_class
    success_url = reverse_lazy("home-link")


class ActivateView(RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.get('username')
        user = get_object_or_404(User, username=username, is_active=False)
        user.is_active = True
        user.save(update_fields=('is_active',))
        user.refresh_from_db()

        return reverse("home-link")
