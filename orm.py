import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Projectorm.settings'  # Reemplaza 'myproject.settings' con la ruta de tu archivo de configuración de Django

import django
django.setup()
from django.db.models import Q, F, FloatField, ExpressionWrapper, Sum, Max, Min, Avg
from django.db.models.functions import Length
from core.models import Periodo, Asignatura, Profesor, Estudiante, Nota, DetalleNota
from datetime import date, timedelta, datetime
from zoneinfo import ZoneInfo


class insertar():
    def insertar_periodos():
        periodos = [
            Periodo(periodo='2024-2025'),
            Periodo(periodo='2023-2024'),
            Periodo(periodo='2022-2023'),
            Periodo(periodo='2021-2022'),
            Periodo(periodo='2020-2021'),
            Periodo(periodo='2019-2020'),
            Periodo(periodo='2018-2019'),
            Periodo(periodo='2017-2018'),
            Periodo(periodo='2016-2017'),
            Periodo(periodo='2015-2016'),
        ]
        periodos_creados = Periodo.objects.bulk_create(periodos)
        print(f'Se han creado {len(periodos_creados)} periodos académicos.')
    def insertar_asignaturas():
        asignaturas = [
            Asignatura(descripcion='Matemáticas'),
            Asignatura(descripcion='Física'),
            Asignatura(descripcion='Programación'),
            Asignatura(descripcion='Literatura'),
            Asignatura(descripcion='Historia'),
            Asignatura(descripcion='Biología'),
            Asignatura(descripcion='Química'),
            Asignatura(descripcion='Geografía'),
            Asignatura(descripcion='Arte'),
            Asignatura(descripcion='Música'),
        ]
        asignaturas_creadas = Asignatura.objects.bulk_create(asignaturas)
        print(f'Se han creado {len(asignaturas_creadas)} asignaturas.')
    
    def insertar_profesores():
        profesores = [
            Profesor(nombre='Luis Rodriguez', cedula = '1234567890'),
            Profesor(nombre='Eduardo Herrera', cedula = '0987654321'),
            Profesor(nombre='Angel Pinina', cedula = '1478523690'),
            Profesor(nombre='Veronica Sagñay', cedula = '3698521470'),
            Profesor(nombre='Jefferson Aguilar', cedula = '2587413690'),
            Profesor(nombre='Wiiliam Rodriguez', cedula = '1234567890'),
            Profesor(nombre='Jordy Yuquilema', cedula = '0987654321'),
            Profesor(nombre='Meche Herrera', cedula = '1478523690'),
            Profesor(nombre='Walter Miño', cedula = '3698521470'),
            Profesor(nombre='Arianna Alvarado', cedula = '2587413690')
    ]
        profesores_creados = Profesor.objects.bulk_create(profesores)
        print(f'Se han creado {len(profesores_creados)} profesores.')
    
    def insertar_estudiantes():
        estudiantes = [
            Estudiante(nombre='Ramon Serra', cedula = '1234567890'),
            Estudiante(nombre='Maria Angela Ribes', cedula = '0987654321'),
            Estudiante(nombre='Juan Carlos Palomo', cedula = '1478523690'),
            Estudiante(nombre='Paula Palacios', cedula = '3698521470'),
            Estudiante(nombre='Eider del Pino', cedula = '2587413690'),
            Estudiante(nombre='Ester Saenz', cedula = '1234567890'),
            Estudiante(nombre='Ana Isabel Arteaga', cedula = '0987654321'),
            Estudiante(nombre='Josue Zambrano', cedula = '1478523690'),
            Estudiante(nombre='Maria Elena Gabarri', cedula = '3698521470'),
            Estudiante(nombre='Juan Angel Valcarcel', cedula = '2587413690')
    ]
        estudiantes_creados = Estudiante.objects.bulk_create(estudiantes)
        print(f'Se han creado {len(estudiantes_creados)} estudiantes.')
    
    def insertar_notas():
        notas = [
            Nota(asignatura = Asignatura.objects.get(pk=1), periodo = Periodo.objects.get(pk=1), profesor = Profesor.objects.get(pk=1)),
            Nota(asignatura = Asignatura.objects.get(pk=2), periodo = Periodo.objects.get(pk=2), profesor = Profesor.objects.get(pk=2)),
            Nota(asignatura = Asignatura.objects.get(pk=3), periodo = Periodo.objects.get(pk=3), profesor = Profesor.objects.get(pk=3)),
            Nota(asignatura = Asignatura.objects.get(pk=4), periodo = Periodo.objects.get(pk=4), profesor = Profesor.objects.get(pk=4)),
            Nota(asignatura = Asignatura.objects.get(pk=5), periodo = Periodo.objects.get(pk=5), profesor = Profesor.objects.get(pk=5)),
            Nota(asignatura = Asignatura.objects.get(pk=6), periodo = Periodo.objects.get(pk=6), profesor = Profesor.objects.get(pk=6)),
            Nota(asignatura = Asignatura.objects.get(pk=7), periodo = Periodo.objects.get(pk=7), profesor = Profesor.objects.get(pk=7)),
            Nota(asignatura = Asignatura.objects.get(pk=8), periodo = Periodo.objects.get(pk=8), profesor = Profesor.objects.get(pk=8)),
            Nota(asignatura = Asignatura.objects.get(pk=9), periodo = Periodo.objects.get(pk=9), profesor = Profesor.objects.get(pk=9)),
            Nota(asignatura = Asignatura.objects.get(pk=10), periodo = Periodo.objects.get(pk=10), profesor = Profesor.objects.get(pk=10))
        ]
        notas_creadas = Nota.objects.bulk_create(notas)
        print(f'Se han creado {len(notas_creadas)} notas.')
    
    def insertar_detallenotas():
        detallenotas = [
            DetalleNota(nota = Nota.objects.get(pk=1), estudiante = Estudiante.objects.get(pk=11), nota1 = 10, nota2 = 7, recuperacion = 8),
            DetalleNota(nota = Nota.objects.get(pk=2), estudiante = Estudiante.objects.get(pk=12), nota1 = 4, nota2 = 10, recuperacion = 6),
            DetalleNota(nota = Nota.objects.get(pk=3), estudiante = Estudiante.objects.get(pk=13), nota1 = 1, nota2 = 5, recuperacion = 3),
            DetalleNota(nota = Nota.objects.get(pk=4), estudiante = Estudiante.objects.get(pk=14), nota1 = 8, nota2 = 7, recuperacion = 9),
            DetalleNota(nota = Nota.objects.get(pk=5), estudiante = Estudiante.objects.get(pk=15), nota1 = 8, nota2 = 9, recuperacion = 10),
            DetalleNota(nota = Nota.objects.get(pk=6), estudiante = Estudiante.objects.get(pk=16), nota1 = 10, nota2 = 10, recuperacion = 10),
            DetalleNota(nota = Nota.objects.get(pk=7), estudiante = Estudiante.objects.get(pk=17), nota1 = 4, nota2 = 6, recuperacion = 5),
            DetalleNota(nota = Nota.objects.get(pk=8), estudiante = Estudiante.objects.get(pk=18), nota1 = 9, nota2 = 9, recuperacion = 9),
            DetalleNota(nota = Nota.objects.get(pk=9), estudiante = Estudiante.objects.get(pk=19), nota1 = 0, nota2 = 9, recuperacion = 5),
            DetalleNota(nota = Nota.objects.get(pk=10), estudiante = Estudiante.objects.get(pk=20), nota1 = 2, nota2 = 10, recuperacion = 6)
        ]
        detallenotas_creadas = DetalleNota.objects.bulk_create(detallenotas)
        print(f'Se han creado {len(detallenotas_creadas)} detalles de notas.')

class consultar_basica():
    def consultar_estudiantes():
        Estudiantes = Estudiante.objects.filter(nombre__startswith='Est')
        for estudiante in Estudiantes:
            print(estudiante.nombre)

    def consultar_profesores():
        Profesores = Profesor.objects.filter(nombre__icontains='or')
        for profesor in Profesores:
            print(profesor.nombre)
    
    def consultar_asignaturas():
        Asignaturas = Asignatura.objects.filter(descripcion__endswith='10')
        for asignatura in Asignaturas:
            print(asignatura.descripcion)
    
    def consultar_Nota1():
        notas = DetalleNota.objects.filter(nota1__gte=8)
        for nota in notas:
            print(nota.nota1)
    
    def consultar_Nota2():
        notas = DetalleNota.objects.filter(nota2__lte=9)
        for nota in notas:
            print(nota.nota2)

    def consultar_recuperacion():
        recuperacion = DetalleNota.objects.filter(recuperacion__gte=9.5)
        for recuperacion in recuperacion:
            print(recuperacion.recuperacion)

class consultar_logica():
    def consultar_estudiante():
        estudiantes = Estudiante.objects.filter(nombre__startswith = "Est",  cedula__endswith='1')
        for estudiante in estudiantes:
            print(estudiante.nombre, estudiante.cedula)
    def consultar_asignatura():
        asignaturas = Asignatura.objects.filter(Q(descripcion__icontains='si') | Q(descripcion__endswith='5'))
        for asignatura in asignaturas:
            print(asignatura.descripcion)
    
    def consultar_profesor():
        profesores = Profesor.objects.exclude(nombre__icontains = "or")
        for profesor in profesores:
            print(profesor.nombre)
    
    def consultar_notas():
        notas = DetalleNota.objects.filter(nota1__gt = 7, nota2__lt = 8)
        for nota in notas:
            print(nota.nota1, nota.nota2)
    
    def consultar_recuperacion():
        recuperaciones = DetalleNota.objects.filter(Q(recuperacion__isnull = True) | Q(nota2__gt = 9) )
        for recuperacion in recuperaciones:
            print(recuperacion.recuperacion, recuperacion.nota2 )

class consultar_funciones():
    def consultar_nota1():
        notas = DetalleNota.objects.filter(nota1__gte = 7, nota1__lte = 9)
        for nota in notas:
            print(nota.nota1)

    def consultar_notafuera():
        notas = DetalleNota.objects.exclude(nota2__gte = 6, nota2__lte = 8)
        for nota in notas:
            print(nota.nota2)
    
    def consultar_recuperacionfuera():
        recuperaciones = DetalleNota.objects.exclude(recuperacion__isnull = True)
        for recuperacion in recuperaciones:
            print(recuperacion.nota)
            print(recuperacion.nota1, recuperacion.nota2)

class consultar_fechas():
    def consultar_año():
        hace_un_año = date.today() - timedelta(days=365)
        notas = DetalleNota.objects.filter(created__gte = hace_un_año)
        for nota in notas:
            print(nota, nota.nota1, nota.nota2)

    def consultar_mes():
        hace_un_mes = date.today() - timedelta(days=30)
        notas = DetalleNota.objects.filter(created__gte = hace_un_mes)
        for nota in notas:
            print(nota, nota.nota1, nota.nota2)
    
    def consultar_dia():
        hace_un_dia = date.today() - timedelta(days=1)
        notas = DetalleNota.objects.filter(created__gte = hace_un_dia)
        for nota in notas:
            print(nota, nota.nota1, nota.nota2)
    
    def consultar_creadasantes():
        inicio = datetime(2024, 1, 1, tzinfo = ZoneInfo("America/Los_Angeles"))
        notas = DetalleNota.objects.filter(created__lt = inicio)
        for nota in notas:
            print(nota.nota1, nota.nota2)
    
    def consultar_creadasmarzo():
        notas = DetalleNota.objects.filter(created__month=3)
        for nota in notas:
            print(nota.nota1, nota.nota2)

class consultar_combinada():
    def consultar_estudiantenombre10():
        estudiantes = Estudiante.objects.annotate(nombre_length=Length('nombre')).filter(nombre_length=10)
        for estudiante in estudiantes:
            print(estudiante.nombre)
    
    def consultar_nota1_nota2():
        detalles = DetalleNota.objects.filter(nota1__gt = 7.5, nota2__gt = 7.5)
        for detalle in detalles:
            print(detalle.nota)
            print(detalle.nota1, detalle.nota2)
    
    def consultar_recuperacion_nonula():
        notas = DetalleNota.objects.exclude(recuperacion__isnull = True).filter(nota1__gt = F('nota2'))
        for nota in notas:
            print(nota.nota)
            print(nota.nota1, nota.nota2)
    
    def consultar_notas():
        notas = DetalleNota.objects.filter(Q(nota1__gt = 8) |Q (nota2 = 7.5) )
        for nota in notas:
            print(nota.nota)
            print(nota.nota1, nota.nota2)

    def consultar_recuperacion_mayor():
        notas = DetalleNota.objects.filter(Q(recuperacion__gt = F("nota1")) & Q(recuperacion__gt = F("nota2")))
        for nota in notas:
            print(nota.nota)
            print(nota.recuperacion)
            print(nota.nota1, nota.nota2)

class consultar_anotaciones():
    def consultar_estudiante_recuperacion():
        estudiantes = Estudiante.objects.filter(detallenota__recuperacion__isnull=False).distinct()
        for estudiante in estudiantes:
            print(estudiante.nombre)

    def consultar_profesor_materia():
        profesores = Profesor.objects.filter(nota__asignatura__descripcion = "Arte").distinct()
        for profesor in profesores:
            print(profesor.nombre)
    
    def consultar_asignatura_no_nula():
        asignaturas = Asignatura.objects.filter(Q(nota__detallenota__nota1__gt = 0) | Q(nota__detallenota__nota2__gt = 0) |Q (nota__detallenota__recuperacion__gt = 0)).distinct()
        for asignatura in asignaturas:
            print(asignatura.descripcion)

    def consultar_asignatura_nula():
        asignaturas = Asignatura.objects.filter(nota__detallenota__nota1__isnull = True, nota__detallenota__nota2__isnull = True, nota__detallenota__recuperacion__isnull = True).distinct()
        for asignatura in asignaturas:
            print(asignatura.descripcion)

    def consultar_estudiante_recuperacion():
        estudiantes = Estudiante.objects.exclude(detallenota__recuperacion__isnull = False)
        for estudiante in estudiantes:
            print(estudiante.nombre)
    
    def consultar_notas_promedio():
        notas = Nota.objects.annotate(promedio = ExpressionWrapper((F("detallenota__nota1") + F("detallenota__nota2")) /2, output_field= FloatField())).filter(promedio__gt = 8)
        for nota in notas:
            print(nota.id, nota.promedio)

    def consultar_nota_mayor():
        notas = DetalleNota.objects.filter(Q(nota1__lt = 6) &Q (nota2__gt = 7))
        for nota in notas:
            print(nota.nota)
            print(nota.nota1, nota.nota2)
    
    def consultar_notas_lista():
        notas = DetalleNota.objects.filter(nota1__in = [7, 8, 9])
        for nota in notas:
            print(f'ID Nota: {nota.id}, Nota1: {nota.nota1}')
    
    def consultar_notas_id():
        notas = DetalleNota.objects.filter(id__range = (21,26))
        for nota in notas:
            print("id:", nota.id, "nota:", nota.nota1)
    
    def consultar_recuperacion_exclude():
        notas = DetalleNota.objects.exclude(recuperacion__in = [8, 9, 10])
        for nota in notas:
            print(nota.recuperacion)
    
    def sumar_notas():
        suma = DetalleNota.objects.filter(estudiante_id = 11).aggregate(Sum("nota1"), Sum("nota2"))
        total = suma["nota1__sum"] + suma["nota2__sum"]
        estudiante = Estudiante.objects.get(id = 11)
        print(estudiante.nombre)
        print(total)

    def nota_maxima(id= 11):
        maxima = DetalleNota.objects.filter(estudiante_id = id).aggregate(Max("nota1"), Max("nota2"))
        max_nota = max(maxima["nota1__max"], maxima["nota2__max"])

        print(max_nota)

    def nota_minima(id= 11):
        minima = DetalleNota.objects.filter(estudiante_id = id).aggregate(Min("nota1"), Min("nota2"))
        min_nota = min(minima["nota1__min"], minima["nota2__min"])

        print(min_nota)
    
    def promedio_notas(id = 11):
        notas = DetalleNota.objects.filter(estudiante_id = id).aggregate(Avg("nota1"), Avg("nota2"))
        promedio_notas = (notas["nota1__avg"] + notas["nota2__avg"]) / 2
        print(promedio_notas)
class subconsultas():
    def obtener_notas(id = 11):
        notas_detalle = DetalleNota.objects.filter(estudiante_id = id).select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in notas_detalle:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')

    def obtener_notas_periodo(id = 8):
        notas_periodo = DetalleNota.objects.filter(nota__periodo__id = id).select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in notas_periodo:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')
            
    def obtener_notas_asignatura(id = 7):
        notas_asignatura = DetalleNota.objects.filter(nota__asignatura__id = id).select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in notas_asignatura:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')

    def obtener_notas_profesor(id = 4):
        notas_profesor = DetalleNota.objects.filter(nota__profesor__id = id).select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in notas_profesor:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')

    def obtener_nota_estudiante(id = 11, valor = 6):
        nota_estudiante = DetalleNota.objects.filter(estudiante__id = id, nota1__gt = valor, nota2__gt = valor).select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in nota_estudiante:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')

    def obtener_nota_ordenada(id = 11):
        nota_estudiante = DetalleNota.objects.filter(estudiante__id = id).order_by("nota__periodo").select_related("nota__asignatura", "nota__periodo", "nota__profesor")
        for nota in nota_estudiante:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')

    def contar_notas(id = 11):
        notas = DetalleNota.objects.filter(estudiante__id = id).count()
        print(f'El estudiante con id {id} tiene {notas} notas.')
    
    def promedio_periodo(id_periodo = 1, id_estudiante = 11):
        promedio = DetalleNota.objects.filter(nota__periodo__id = id_periodo, estudiante__id = id_estudiante).aggregate(Avg("nota1"), Avg("nota2"))
        promedio_total = (promedio["nota1__avg"] + promedio["nota2__avg"]) / 2
        print(f'El promedio de las notas del estudiante con id {id_estudiante} en el período {id_periodo} es {promedio_total}.')

    def nota_observacion(observacion_user = "hola"):
        notas = DetalleNota.objects.filter(observacion = observacion_user).select_related("nota__asignatura", "nota__periodo", "nota__profesor", "estudiante")
        for nota in notas:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}, Observacion: {nota.observacion}')

    def notas_ordenadas_asignatura(id_estudiante = 11):
        notas_ordenadas = DetalleNota.objects.filter(estudiante__id = id_estudiante).order_by("nota__asignatura")
        for nota in notas_ordenadas:
            print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.descripcion}, Periodo: {nota.nota.periodo.periodo}, Profesor: {nota.nota.profesor.nombre}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')
class sentencias_update():
    def actualizar_nota1(valor = 20):
        try:
            DetalleNota.objects.filter(nota1__lt = 20).update(nota1 = valor)
            print("las notas se han actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al actualizar las notas: {e}")

    def actualizar_nota2(valor = 15):
        try:
            DetalleNota.objects.filter(nota2__lt = 15).update(nota2 = valor)
            print("las notas se han actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al actualizar las notas: {e}")
    
    def actualizar_recuperacion(valor = 8):
        try:
            DetalleNota.objects.filter(recuperacion__lt = 10).update(recuperacion = valor)
            print("las notas se han actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al actualizar las notas: {e}")
    
    def actualizar_observacion():
        try:
            DetalleNota.objects.filter(nota1__gte = 10, nota2__gte = 10).update(observacion = "Aprobado")
            print("Las observaciones se han actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar las observaciones: {e}")
    
    def actualizar_periodo(id = 3, nuevo_nota1 = 7, nuevo_nota2 = 9):
        try:
            DetalleNota.objects.filter(nota__periodo__id = id).update(nota1 = nuevo_nota1, nota2 = nuevo_nota2)
            print("Las notas se han actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar las notas: {e}")

class sentencias_delete():
    def eliminar_nota_estudiante(id_estudiante):
        try:
            DetalleNota.objects.filter(estudiante__id = id_estudiante).delete()
            print("Las notas del estudiante se han eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar las notas del estudiante: {e}")
    
    def eliminar_nota_logica(id_estudiante):
        try:
            DetalleNota.objects.filter(estudiante__id = id_estudiante).update(state = False)
            print("Las notas del estudiante se han desactivado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al desactivar las notas del estudiante: {e}")
    
    def eliminar_nota_periodo_fisico(id_periodo):
        try:
            DetalleNota.objects.filter(nota__periodo__id = id_periodo).delete()
            print("Las notas del período se han eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar las notas del período: {e}")
    
    def eliminar_nota_periodo_logico(id_periodo):
        try:
            DetalleNota.objects.filter(nota__periodo__id = id_periodo).update(state = False)
            print("Las notas del período se han eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar las notas del período: {e}")
    
    def eliminar_nota_menor_fisica():
        try:
            DetalleNota.objects.filter(nota1__lt = 10).delete()
            print("Las notas con nota1 menor a 10 se han eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar las notas: {e}")

class sentencias_crud():
    def insertar_nota_estudiante(id_estudiante = 19, id_asignatura = 2, id_periodo = 3, id_profesor = 5, nota1 = 10, nota2 = 9):
        try:
            estudiante = Estudiante.objects.get(id=id_estudiante)
            asignatura = Asignatura.objects.get(id=id_asignatura)
            periodo = Periodo.objects.get(id=id_periodo)
            profesor = Profesor.objects.get(id=id_profesor)
    
            nota = Nota(
                asignatura=asignatura,
                periodo=periodo,
                profesor=profesor
            )
            nota.save()
    
            detalle_nota = DetalleNota(
                nota=nota,
                nota1=nota1,
                nota2=nota2,
                estudiante=estudiante
            )
            detalle_nota.save()
            print("La nota del estudiante se ha insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la nota del estudiante: {e}")
#-----Insertar registros------
#insertar.insertar_periodos()
#insertar.insertar_asignaturas()
#insertar.insertar_profesores()
#insertar.insertar_estudiantes()
#insertar.insertar_notas()
#insertar.insertar_detallenotas()

#-----Consultar basicas-----
#consultar_basica.consultar_estudiantes()
#consultar_basica.consultar_profesores()
#consultar_basica.consultar_asignaturas()
#consultar_basica.consultar_Nota1()
#consultar_basica.consultar_Nota2()
#consultar_basica.consultar_recuperacion()

#-----Consultas usando condiciones lógicas (AND, OR, NOT)-----
#consultar_logica.consultar_estudiante()
#consultar_logica.consultar_asignatura()
#consultar_logica.consultar_profesor()
#consultar_logica.consultar_notas()
#consultar_logica.consultar_recuperacion()

#-----Consultas usando funciones numéricas-----
#consultar_funciones.consultar_nota1()
#consultar_funciones.consultar_notafuera()
#consultar_funciones.consultar_recuperacionfuera()

#-----Consultas usando funciones de fecha-----
#consultar_fechas.consultar_año()
#consultar_fechas.consultar_mes()
#consultar_fechas.consultar_dia()
#consultar_fechas.consultar_creadasantes()
#consultar_fechas.consultar_creadasmarzo()

#-----Consultas combinadas con funciones avanzadas-----
#consultar_combinada.consultar_estudiantenombre10()
#consultar_combinada.consultar_nota1_nota2()
#consultar_combinada.consultar_recuperacion_nonula()
#consultar_combinada.consultar_notas()
#consultar_combinada.consultar_recuperacion_mayor()

#-----Consultas con subconsultas y anotaciones-----
#consultar_anotaciones.consultar_estudiante_recuperacion()
#consultar_anotaciones.consultar_profesor_materia()
#consultar_anotaciones.consultar_asignatura_no_nula()
#consultar_anotaciones.consultar_asignatura_nula()
#consultar_anotaciones.consultar_estudiante_recuperacion()
#consultar_anotaciones.consultar_notas_promedio()
#consultar_anotaciones.consultar_nota_mayor()
#consultar_anotaciones.consultar_notas_lista()
#consultar_anotaciones.consultar_notas_id()
#consultar_anotaciones.consultar_recuperacion_exclude()
#consultar_anotaciones.sumar_notas()
#consultar_anotaciones.nota_maxima(15)
#consultar_anotaciones.nota_minima()
#consultar_anotaciones.promedio_notas()

#-----Consultas con subconsultas con los modelos relacionado-----
#subconsultas.obtener_notas()
#subconsultas.obtener_notas_periodo()
#subconsultas.obtener_notas_asignatura()
#subconsultas.obtener_notas_profesor(7)
#subconsultas.obtener_nota_estudiante()
#subconsultas.obtener_nota_ordenada()
#subconsultas.contar_notas()
#subconsultas.promedio_periodo()
#subconsultas.nota_observacion()
#subconsultas.notas_ordenadas_asignatura()

#-----Sentencias Update-----
#sentencias_update.actualizar_nota1()
#sentencias_update.actualizar_nota2(5)
#sentencias_update.actualizar_recuperacion(7)
#sentencias_update.actualizar_observacion()
#sentencias_update.actualizar_periodo()

#-----Sentencias delete-----
#sentencias_delete.eliminar_nota_estudiante(20)
#sentencias_delete.eliminar_nota_logica(18)
#sentencias_delete.eliminar_nota_periodo_fisico(3)
#sentencias_delete.eliminar_nota_periodo_logico(2)
#sentencias_delete.eliminar_nota_menor_fisica()

#-----Sentencias crud:-----
#sentencias_crud.insertar_nota_estudiante()
