from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    #url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$', 'app.views.home', name='home'), 

    url(r'^equipo_create$', 'app.views.equipo_create', name='equipo_create'), 
    url(r'^equipo_edit$', 'app.views.equipo_edit'    , name='equipo_edit'),  

    
    url(r'^auto/(\d+)$', 'app.views.auto', name='auto'), 
    url(r'^auto_create/(\d+)$', 'app.views.auto_create', name='auto_create'), 
    url(r'^auto_edit$', 'app.views.auto_edit'    , name='auto_edit'), 

    url(r'^geomyride$', 'app.views.geomyride', name='geomyride'),  

    #url(r'^monitor/', 'app.views.monitor', name='monitor'),
    #url(r'^GeoMyRide/', include('GeoMyRide.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/(?P<username>[-\w]+)/$', 'bookmark_user',
        name='marcador_bookmark_user'),
    #url(r'^$', 'bookmark_list', name='marcador_bookmark_list'),
)


urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
)
