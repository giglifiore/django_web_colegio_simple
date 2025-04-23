#from django.conf.urls import include
from django.urls import path

from django.contrib import admin

from inicio import views

admin.autodiscover()

urlpatterns = patterns('',
   
   # url(r'^$', views.inicio, name="inicio_redirect"),
    path('ameliagallegos/', include('inicio.urls', namespace='inicio')),
    path('sisacademico/', include('sisacademico.urls', namespace='sisacademico')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alumnos'),
)
