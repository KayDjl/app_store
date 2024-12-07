from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


from goods.models import Categories


class indexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Магазин мебели Home'
        return context

class aboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] =  'Home - О нас'
        context["content"] =  'О нас'
        context["text_on_page"] =  'Текст о том почему этот магазин такой классный, и какой хороший товар'
        return context
