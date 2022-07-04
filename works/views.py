from django.shortcuts import render
from .models import WorksModel
from django.views.generic import ListView, DetailView


class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
    paginate_by = 10


class WorkDetailView(DetailView):
    model = WorksModel
    template_name = 'main/work_in.html'

