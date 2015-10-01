# -*- coding: cp1252

def main():
    """El usuario ingresa la tarifa por segundo, cuántas
       comunicaciones se realizaron. y la duración de cada
       comunicación expresadas en horas. minutos y segundos.Como resultado se informa la duración en
       segundos de cada comunicación y su costo."""

    f = input("¿Cuánto cuesta 1 segundo de comunicación?: ")
    n = input("¿Cuántas comunicaciones hubo?: ")
    total = 0
    for x in range(n):
        hs = input("¿Cuántas horas?: ")
        min = input("¿Cuántos minutos?: ")
        seg = input("¿Cuántos segundos?: ")
        segcalc = asegundos(hs, min, seg)
        costo = segcalc * f
        pesos = int(costo)
        centavos = abs(costo)-abs(int(costo))
        print "Duracion: ", segcalc, "segundos. Costo: ",pesos,
        total = costo + total
        pass
    print "La suma total de las comunicaciones es: ", total,

def asegundos (horas, minutos, segundos):
    segsal = 3600 * int(horas) + 60 * int(minutos) + int(segundos)
    return segsal

main()
