from django.forms import ModelForm,CharField, Form
from django.forms.forms import BoundField
from django.forms.util import ErrorList
from django.template import Context, Template
 
from functools import partial
from .models import *


class EquiposForm(ModelForm):
    class Meta:
        model = Equipo
        exclude = ('usuario_id', 'created', 'modified')

    def __init__(self, *args, **kwargs):
        self._usuario_id = kwargs.pop('usuario_id', None)
        super(EquiposForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.instance.pk:
            if not self._usuario_id:
                raise TypeError('No hay usuario asignado')
            self.instance.usuario_id = self._usuario_id
        return super(EquiposForm, self).save(commit)    

class AutosForm(ModelForm):
    class Meta:
        model = Auto
        exclude = ('equipo_id', 'created', 'modified','aprs','activo')

    def __init__(self, *args, **kwargs):
        self._equipo_id = kwargs.pop('equipo_id', None)
        super(AutosForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.instance.pk:
            if not self._equipo_id:
                raise TypeError('No hay equipo asignado')
            self.instance.equipo_id = self._equipo_id
        return super(AutosForm, self).save(commit)    

class SignUp(ModelForm):
    class Meta:
        model = User
        exclude = ('usuario_id', 'created', 'modified')

    def __init__(self, *args, **kwargs):
        self._usuario_id = kwargs.pop('usuario_id', None)
        super(EquiposForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.instance.pk:
            if not self._usuario_id:
                raise TypeError('No hay usuario asignado')
            self.instance.usuario_id = self._usuario_id
        return super(EquiposForm, self).save(commit)    