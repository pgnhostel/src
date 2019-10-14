from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Pgs, Area


class PgsListView(ListView):
    model = Pgs
    template_name = 'home.html'


class PgsDetailView(DetailView):
    model = Pgs
    template_name = 'pg_detail.html'

