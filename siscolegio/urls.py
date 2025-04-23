#from django.conf.urls import include
from django.urls import path

from django.contrib import admin

from inicio import views

admin.autodiscover()

urlpatterns = patterns('',
   
   # url(r'^$', views.inicio, name="inicio_redirect"),
    #url(r'^ameliagallegos/', include('inicio.urls', namespace='inicio')),
    #url(r'^sisacademico/', include('sisacademico.urls', namespace='sisacademico')),
    #url(r'^admin/', include(admin.site.urls)),
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alumnos'),
)
