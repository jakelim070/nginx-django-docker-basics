from django.urls import path

from . import views

app_name = "outhouse"

urlpatterns = [
    path(
        "vendors/",
        views.VendorListView.as_view(),
        name="vendor_list",
    ),
    path(
        "vendors/create/",
        views.VendorCreateView.as_view(),
        name="vendor_create",
    ),
    path(
        "vendors/<int:pk>/",
        views.VendorDetailView.as_view(),
        name="vendor_detail",
    ),
]
