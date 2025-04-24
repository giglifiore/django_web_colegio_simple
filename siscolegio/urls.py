from django.contrib import admin
from django.urls import path, include
from sisacademico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    #path('', include('inicio.urls', namespace='inicio')),  # Página de inicio
    path('ameliagallegos/', include('inicio.urls', namespace='inicio')),
    path('sisacademico/', include('sisacademico.urls', namespace='sisacademico')),
]
