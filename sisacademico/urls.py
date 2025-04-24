# -*- coding: utf-8 -*-
from django.urls import re_path  # usamos re_path para expresiones regulares
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from sisacademico import views
app_name = 'sisacademico'
urlpatterns = [
    re_path(r'^alumno_notas/$', views.reporte_alumno_notas, name='alumno_notas'),
    re_path(r'^reporte_quimestre/$', views.reporte_quimestre, name='reporte_quimestre'),
    re_path(r'^reporte_matricula/$', views.reporte_matricula, name='reporte_matricula'),
    re_path(r'^alumnos/(?P<tipo_reporte>\w+)/$', views.alumnos, name='alumnos'),

    re_path(r'^authcheck/$', views.authcheck, name='authcheck'),
    re_path(r'^cambiar_password/password_changed/$', views.password_changed, name='password_changed'),
    
    re_path(r'^cambiar_password/$', PasswordChangeView.as_view(
        template_name='sisacademico/cambiar_password.html',
        success_url='password_changed/',
        form_class=PasswordChangeForm
    ), name='cambiar_password'),

    re_path(r'^perfil_profesor/$', views.perfil_profesor, name='perfil_profesor'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^clases/$', views.clases, name='clases'),
    re_path(r'^clase/(?P<clase_id>\d+)/(?P<periodo_id>\d+)/$', views.clase_alumnos, name='clase_alumnos'),
    re_path(r'^clase/(?P<clase_id>\d+)/$', views.clase_periodos, name='clase_periodos'),
    re_path(r'^editar_notas/$', views.editar_notas, name='editar_notas'),

    re_path(r'^matricular_grupo/$', views.matricular_grupo, name='matricular_grupo'),
    re_path(r'^publicar_nota/$', views.publicar_nota, name='publicar_nota'),
    re_path(r'^esconder_nota/$', views.esconder_nota, name='esconder_nota'),
]

