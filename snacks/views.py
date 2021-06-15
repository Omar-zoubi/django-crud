from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Snack

# Create your views here.
class HomeListView(ListView):
    template_name= 'list.html'
    model = Snack
class DetailsListView(DetailView):
    template_name = 'details.html'
    model = Snack
class CreateListView(CreateView):
    template_name = 'create.html'
    model = Snack
    fields = ["title","purcheser","description"]
class UpdateListView(UpdateView):
    template_name = 'update.html'
    model = Snack
    fields = ["title","purcheser","description"]
class DeleteListView(DeleteView):
    template_name = 'delete.html'
    model = Snack
    success_url = reverse_lazy("list")


