from django.urls import path

from . import views

app_name = "materials"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "parts/",
        views.EnginePartListView.as_view(),
        name="engineparts_list",
    ),
    path(
        "parts/create/",
        views.EnginePartCreateView.as_view(),
        name="engineparts_create",
    ),
    path(
        "parts/<int:pk>/",
        views.EnginePartDetailView.as_view(),
        name="engineparts_detail",
    ),
]
