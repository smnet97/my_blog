from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from .forms import MessageModelForm
from .models import MessageModel
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from .utils import send_bot_message
from works.models import WorksModel
from blogs.models import BlogModel


class HomeView(ListView):
    template_name = 'main/home.html'
    queryset = WorksModel.objects.all().order_by('-id')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = BlogModel.objects.all().order_by('-id')[:2]
        return data

class ContactView(CreateView):
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse("contact")


    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Salom {form.instance.name} ! Xabaringiz qabul qilindi."
        # send_mail("Test", message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)
