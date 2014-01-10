"""from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def geomy(request):
    dajax = Dajax()
    result = request
    return simplejson.dumps({'id':result})

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})
"""