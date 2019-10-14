from django.shortcuts import render
from django.views.generic import ListView
from . models import Faq


class FaqListView(ListView):
    model = Faq
    template_name = 'faq.html'





