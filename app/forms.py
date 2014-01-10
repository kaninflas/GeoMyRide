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


class BootstrapForm(Form):
    template = \
u'''
{%for field in form%}
<div class="control-group {%if field.errors%}error{%endif%}">
{{field.label_tag}}
<div class="controls">
{{field}}<span class="help-inline">{{field.errors}}</span>
</div>
</div>
{% endfor %}
'''
 
    def __unicode__(self):
        c = Context({'form': self})
        t = Template(self.template)
        return t.render(c)
 
 
def decorate_label_tag(f):
 
    def bootstrap_label_tag(self, contents=None, attrs=None):
        attrs = attrs or {}
        add_class(attrs, 'control-label')
        return f(self, contents, attrs)
 
    return bootstrap_label_tag
 
 
BoundField.label_tag = decorate_label_tag(
         BoundField.label_tag)
 
 
def add_class(attrs, html_class):
    assert type(attrs) is dict
 
    if 'class' in attrs:
        classes = attrs['class'].split()
        if not html_class in classes:
            classes.append(html_class)
            attrs['class'] = ' '.join(classes)
    else:
        attrs['class'] = html_class
 
 
class BootstrapErrorList(ErrorList):
 
    def __unicode__(self):
        if not self:
            return u''
        return u' '.join(unicode(e) for e in self)
 
 
class NameForm(BootstrapForm):
    first_name = CharField()
    last_name = CharField()
 
TeamForm = partial(EquiposForm, error_class=BootstrapErrorList)