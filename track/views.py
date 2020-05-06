import logging
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    #logger.debug('index init')
    
    try:
        return render(request, "index.html", None) 
    except:
        logger.exception('')

def test(request, name):
    r= None
    
    try:
        raise Exception('Log my raised ex')
    except Exception as e:
        r=str(e)
        logger.exception('')

    r = "name = {0} -  ex: {1}".format(name, r)
    return HttpResponse(r)
