from django.db import models

class ActiveManager(models.Manager):
        def get_queryset(self):
                return super().get_queryset().filter(state=True)

class BaseModel(models.Model):
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = 1)
        state = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        objects = models.Manager()
        active_objects = ActiveManager()

        def delete(self, *args, **kwargs):
                self.state = False
                self.save()

        class Meta:
                abstract = True

class Asignatura(BaseModel):
        descripcion = models.CharField(max_length=50)

        def __str__(self):
                return self.descripcion

class Periodo(BaseModel):
        periodo = models.CharField(max_length=50)

        def __str__(self):
                return "periodo" + self.periodo

class Profesor(BaseModel):
        nombre = models.CharField(max_length=50)
        cedula = models.CharField(max_length=10)

        def __str__(self):
                return self.nombre

class Estudiante(BaseModel):
        nombre = models.CharField(max_length=50)
        cedula = models.CharField(max_length=10)

        def __str__(self):
                return self.nombre

class Nota(BaseModel):
        asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
        periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
        profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
        def __str__(self):
                return "Notas de " + self.asignatura.descripcion + " - Periodo Lectivo " + self.periodo.periodo + " - Profesor " + self.profesor.nombre

class DetalleNota(BaseModel):
        nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
        nota1 = models.FloatField(default=0.0)
        nota2 = models.FloatField(default=0.0)
        estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
        recuperacion = models.FloatField(default=0.0)
        observacion = models.TextField()

        def __str__(self):
                return "Nota de " + self.estudiante.nombre + " en " + self.nota.asignatura.descripcion