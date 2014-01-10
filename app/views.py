from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.template.context import RequestContext
from django.core.exceptions import PermissionDenied

from django.utils import simplejson
from django.utils.dateformat import DateFormat
from models import *
from django.db.models import Q
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import urllib2



def home(request):  
    template = "geomyride/landing.html"
    if request.user.is_authenticated():        
        equipos  = Equipo.objects.filter(usuario_id = request.user).order_by('-modified')
        #equipos  = Equipo.objects.select_related('pk','auto__equipo_id').filter(usuario_id = request.user).order_by('-modified')
        
        """
        for val in equipos:
        	val.auto_set.all()
        	equipos[val.id - 1].auto = val
        """

        
        context  = {'equipos': equipos, "request":request}    
        template = "geomyride/index.html"
    else:
        template = "geomyride/landing.html"
        context  = {}
    return render(request,template,context)

@login_required
def equipo_create(request):
    if request.method == 'POST':
        form = EquiposForm(usuario_id=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquiposForm()

    data = {'title':'Equipo', 'url': 'equipo_create'}
    return render(request, 'geomyride/form.html',
        {'form': form, 'create': True, 'data': data})

@login_required
def equipo_edit(request, pk):
    data = get_object_or_404(Equipo, pk=pk)
    if equipo.usuario_id != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = EquiposForm(instance=data, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquiposForm(instance=data)


    data.tipo = 'Equipo'
    data.url = 'equipo_edit'
    return render(request, 'geomyride/form.html',
        {'form': form, 'create': False, 'data': data})

@login_required
def auto(request,id):
    autos = Auto.objects.get(pk = id);
    recorridos = Recorrido.objects.filter(auto_id = id).order_by('timestamp')
    
    return render(request, 'geomyride/auto.html', {'autos': autos,'recorridos':recorridos})

@login_required
def auto_create(request,id_equipo):
    if request.method == 'POST':
        form = AutosForm(equipo_id=Equipo.objects.get(id=id_equipo), data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutosForm()

    
    data = {'title':'Auto', 'url': 'auto_create/'+id_equipo}
    return render(request, 'geomyride/form.html',
        {'form': form, 'create': True, 'data': data})

@login_required
def auto_edit(request, pk):
    data = get_object_or_404(Auto, pk=pk)
    if data.usuario_id != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = AutosForm(instance=data, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutosForm(instance=data)

    data.title = 'Auto'
    data.url = 'auto_edit'
    return render(request, 'geomyride/form.html',
        {'form': form, 'create': False, 'data': data})



@login_required
def geomyride(request):
    if request.method == "GET":
    	id_recorrido = request.GET['id']
    else:
    	id_recorrido = ""


    qs = Recorrido.objects.get(pk = id_recorrido)

    recorridos = Recorrido.objects.filter(
    	Q(auto_id= qs.auto_id),
    	Q(timestamp__year = qs.timestamp.year),
    	Q(timestamp__month= qs.timestamp.month),
    	Q(timestamp__day  = qs.timestamp.day)
    ).order_by('-timestamp')

    to_json = []
    for dog in recorridos:
        # for each object, construct a dictionary containing the data i will return
        dog_dict = {}
        dog_dict['auto_id']   = dog.auto_id_id
        dog_dict['lan']       = dog.longitud
        dog_dict['timestamp'] = DateFormat(dog.timestamp).format('Y-m-d H:i:s')
        dog_dict['aprs']      = dog.aprs
        dog_dict['lat']       = dog.latitud
        dog_dict['speed']     = dog.speed
        dog_dict['id']        = dog.pk

        to_json.append(dog_dict)

    # convert the list to JSON
    # return an HttpResponse with the JSON and the correct MIME type
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')



"""
def monitor(request):
	response = urllib2.urlopen('http://api.aprs.fi/api/get?name=IZ2XSB-9&what=loc&apikey=58417.RaAR1shOeKd7kO&format=json')
	html = response.read()
	resultado = Recorrido.objects.all()
	template = "monitor.html"
	return render(request, template,{"resultado" : html, "request":request, "serial":ser.portstr})
"""
