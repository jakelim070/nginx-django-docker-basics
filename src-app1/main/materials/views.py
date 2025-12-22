from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from . import models


def index(request):
    return HttpResponse("Hello, world. You're at the materials index.")


class EnginePartListView(generic.ListView):
    model = models.EnginePart
    template_name = "materials/part-list.html"
    context_object_name = "parts"


class EnginePartCreateView(generic.CreateView):
    model = models.EnginePart
    fields = ["part_number", "description", "material_type"]
    template_name = "materials/part-form.html"
    success_url = "/materials/parts/"


class EnginePartDetailView(generic.DetailView):
    model = models.EnginePart
    template_name = "materials/part-detail.html"
    context_object_name = "part"
