from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse

import datetime


def hello(request, param1, param2):
    t = get_template("home.html")

    x = {1,2,3,4}

    c = {"param1": param1, "param2": param2, "show": False, "x": x}
    html = t.render(c)

    return HttpResponse(html)


def index(request):
    return HttpResponse("Is index page.")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
