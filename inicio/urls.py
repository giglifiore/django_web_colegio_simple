from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name="inicio_redirect"),
    path('inicio/', views.inicio, name='inicio'),
    path('colegio/', views.colegio, name='colegio'),
    path('docentes/', views.docentes, name='docentes'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('blog/', views.blog, name='blog'),
    path('sislogin/', views.sislogin, name='sislogin'),
]
