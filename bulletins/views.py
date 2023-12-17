from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from bulletins.forms import BulletinForm

from .models import Bulletin


class BulletinListView(ListView):
    model = Bulletin
    template_name = "bulletins/index.html"
    context_object_name = "bulletins"


class BulletinCreateView(LoginRequiredMixin, CreateView):
    model = Bulletin
    form_class = BulletinForm
    template_name = "bulletins/bulletin_form.html"
    success_url = reverse_lazy("bulletin_list")


class BulletinUpdateView(LoginRequiredMixin, UpdateView):
    model = Bulletin
    form_class = BulletinForm
    template_name = "bulletins/bulletin_form.html"
    form_class = BulletinForm
    success_url = reverse_lazy("bulletin_list")


class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletin
    form_class = BulletinForm
    template_name = "bulletins/bulletin_confirm_delete.html"
    success_url = reverse_lazy("bulletin_list")

