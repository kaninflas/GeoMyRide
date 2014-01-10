from django.contrib import admin
from models import Equipo,Auto,Recorrido
import thread, time


class EnlaceAdmin(admin.ModelAdmin):
	list_display  = ('nombre', 'descripcion','created','usuario_id')
	list_filter   = ('nombre', 'usuario_id')
	search_fields = ('nombre__usuario_id','nombre')
	raw_id_fields = ('usuario_id',)

class EnlaceAuto(admin.ModelAdmin):
	list_display  = ('modelo','marca','created', 'equipo_id')
	list_filter   = ('modelo','marca', 'equipo_id')
	search_fields = ('modelo__equipo_id','marca__modelo')
	raw_id_fields = ('equipo_id',)

class EnlaceRecorrido(admin.ModelAdmin):
	list_display = ('aprs','latitud','longitud', 'timestamp')
	list_filter = ('aprs',)
	search_fields = ('aprs',)

	"""
	def aprs(self, obj):
		v = obj.get_aprs()
		tag = '<a id="%s" class="map" href="javascript:void(0)" onClick="startMonitor(\'%s\')">Monitorear</a>' % (v,v)
		return tag

	aprs.allow_tags = True
	"""

admin.site.register(Equipo,EnlaceAdmin)
admin.site.register(Auto,EnlaceAuto)
admin.site.register(Recorrido,EnlaceRecorrido)