from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),     
    url(r'^register$', 'app.views.register'    , name='register'), 

    url(r'^equipo_create$', 'app.views.equipo_create', name='equipo_create'), 
    url(r'^equipo_edit$', 'app.views.equipo_edit'    , name='equipo_edit'),  

    
    url(r'^auto/(\d+)$', 'app.views.auto', name='auto'), 
    url(r'^auto_create/(\d+)$', 'app.views.auto_create', name='auto_create'), 
    url(r'^auto_edit$', 'app.views.auto_edit'    , name='auto_edit'), 

    url(r'^geomyride$', 'app.views.geomyride', name='geomyride'),  


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
)
