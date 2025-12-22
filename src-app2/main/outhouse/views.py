from django.shortcuts import render
from django.views import generic

from . import models

# Create your views here.


class VendorListView(generic.ListView):
    model = models.VendorModel
    template_name = "outhouse/vendor-list.html"
    context_object_name = "vendors"


class VendorCreateView(generic.CreateView):
    model = models.VendorModel
    fields = ["name", "address"]
    template_name = "outhouse/vendor-create.html"
    success_url = "/outhouse/vendors/"


class VendorDetailView(generic.DetailView):
    model = models.VendorModel
    template_name = "outhouse/vendor-detail.html"
    context_object_name = "vendor"
