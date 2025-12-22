from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "App1 landing page <a href='/materials/'>Go to Materials App</a>"
    )
