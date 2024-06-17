from django.contrib import admin
from .models import Asignatura, DetalleNota, Estudiante, Nota, Periodo, Profesor

admin.site.register(Asignatura)
admin.site.register(DetalleNota)
admin.site.register(Estudiante)
admin.site.register(Nota)
admin.site.register(Periodo)
admin.site.register(Profesor)
