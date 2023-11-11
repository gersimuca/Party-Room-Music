from django.shortcuts import render
from django.views.generic.base import TemplateView
from dv.models import Books
# Create your views here.

class IndexView(TemplateView):
    tempate_name = "dv/home.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(self, **kwargs)
        contex['books'] = Books.objects.all()
        return contex
