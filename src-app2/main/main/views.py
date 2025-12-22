from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "App2 landing page <br> <a href='/outhouse/vendors/'>Go to Outhouse App</a>"
    )
