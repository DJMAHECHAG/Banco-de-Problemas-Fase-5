#BANCO DE PROBLEMAS DE PROGRAMACION #5
#MATRIZ:
#[Nombre, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo]
recursos = [
    ["Paula", 7, 8, 5, 10, 6, 4, 3],
    ["Juliana", 5, 6, 7, 8, 9, 10, 11],
    ["Luciana", 6, 7, 8, 9, 10, 11, 12],
    ["Julio", 4, 5, 3, 2, 1, 0, 0]
]
#CALCULO DE HORAS Y CLASIFICACION
def calcular_horas_y_clasificar(recursos):
    nombre = recursos[0]
    horas = recursos[1:]
    total_horas = sum(horas)
    #CLASIFICACION
    if total_horas >= 40:
        clasificacion = "Sobretiempo"
    else: clasificacion = "Horario estandar"

    #RETORNO DE RESULTADOS
    return nombre, total_horas, clasificacion

print("REPORTE SEMANAL DE HORAS\n")
for recurso in recursos:
    nombre, total_horas, clasificacion = calcular_horas_y_clasificar(recurso)

#RESULTADOS
    print("Nombre:", nombre)
    print("Total de horas:", total_horas)
    print("Clasificación:", clasificacion)
    print()