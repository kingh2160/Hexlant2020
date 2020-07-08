from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def index(req):
    template = loader.get_template('index.html')
    now = datetime.now()
    print((now))
    context = {
        'current_date' : now,
        "value" : 2,
    }
    return HttpResponse(template.render(context,req))
