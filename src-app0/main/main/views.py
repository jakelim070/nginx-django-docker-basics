from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse(
        "App1 landing page <a href='/materials/'>Go to Materials App</a>"
    )


class LandingPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Define your apps here.
        # This makes it easy to add "App 3" later without touching HTML.
        context["apps"] = [
            {
                "name": "Application 1",
                "description": "Access the first dashboard environment.",
                "url": "/app1/",
                "icon": "fa-rocket",  # FontAwesome class
                "btn_class": "btn-outline-primary",
                "bg_class": "bg-primary",
            },
            {
                "name": "Application 2",
                "description": "Access the second dashboard environment.",
                "url": "/app2/",
                "icon": "fa-layer-group",  # FontAwesome class
                "btn_class": "btn-outline-success",
                "bg_class": "bg-success",
            },
        ]

        return context
