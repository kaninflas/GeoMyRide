from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    usuario_id  = models.ForeignKey(User)
    nombre      = models.CharField(max_length = 140)
    descripcion = models.CharField(max_length = 140)
    created     = models.DateTimeField(auto_now_add=True) 
    modified    = models.DateTimeField(auto_now_add=True) 
    
    def __unicode__(self):
        return "%s" % (self.nombre)

class Auto(models.Model):
    equipo_id = models.ForeignKey(Equipo)
    modelo    = models.CharField(max_length = 140)
    marca     = models.CharField(max_length = 140)
    aprs      = models.CharField(max_length = 140)
    created   = models.DateTimeField(auto_now_add=True) 
    modified  = models.DateTimeField(auto_now_add=True)
    activo    = models.IntegerField(default = 0)

    def __unicode__(self):
        return "%s" % (self.modelo)

    def es_activo(self):
        if self.activo == 1:
            return True
        else:
            return False

class Recorrido(models.Model):
    auto_id  = models.ForeignKey(Auto)
    aprs     = models.CharField( max_length = 140)
    latitud  = models.FloatField();
    longitud = models.FloatField();
    speed    = models.FloatField()
    timestamp= models.DateTimeField(auto_now_add=True)  

    def get_aprs(self):
        return self.auto_id

    def __unicode__(self):
        return "{'id': %s, 'lat': %s ,'lan':  %s, 'timestamp':%s}" % (self.pk,self.latitud,self.longitud,self.timestamp)

class Simulador(models.Model):
    auto_id  = models.ForeignKey(Auto)
    aprs     = models.CharField( max_length = 140)
    latitud  = models.FloatField();
    longitud = models.FloatField();
    speed    = models.FloatField()
    timestamp= models.DateTimeField(auto_now_add=True)  

    def get_aprs(self):
        return self.auto_id

    def __unicode__(self):
        return "{'id': %s, 'lat': %s ,'lan':  %s, 'timestamp':%s}" % (self.pk,self.latitud,self.longitud,self.timestamp)


