import sys
from manejo_de_datos.constantes import *
import manejo_de_datos.mostrar_datos_stdin as md
import manejo_de_datos.crear_archivos as ca
from vamosmoshi_programa import VamosMoshi


def ejecutar(archivo_mapa):
    nombre_a_ciudad = {}
    programa = VamosMoshi(archivo_mapa, nombre_a_ciudad)

    while True:
        try:
            ingreso = input().lower()
        except EOFError:
            break

        comando, parametros = ingreso.split()[0], ingreso.split()[1:]

        if comando == IR:  # ir desde, hasta, archivo
            try:
                desde = nombre_a_ciudad[parametros[0].rstrip(',').capitalize()]
                hasta = nombre_a_ciudad[parametros[1].rstrip(',').capitalize()]

                tiempo, padres = programa.camino_minimo(desde, hasta)

                if tiempo is None:
                    print(RECORRIDO_NO_ENCONTRADO)
                else:
                    print(md.mostrar_camino(padres, hasta, tiempo=tiempo))
                    ca.crear_archivo_kml(parametros[2], desde, hasta, padres)
            except KeyError:
                print(RECORRIDO_NO_ENCONTRADO)

        elif comando == ITINERARIO:  # itinerario recomendaciones.csv
            recomendaciones = parametros[0]
            itinerario = programa.itinerario_recomendaciones(recomendaciones)
            if itinerario is None:
                print(RECORRIDO_NO_ENCONTRADO)
            else:
                print(md.mostrar_camino(camino_lista=itinerario))

        elif comando == VIAJE:  # viaje origen, archivo
            origen, archivo_nombre = parametros[0], parametros[1]
            try:
                origen = nombre_a_ciudad[parametros[0].rstrip(
                    ',').capitalize()]

                recorrido, tiempo_total = programa.recorrido_completo(origen)
                if recorrido is None:
                    print(RECORRIDO_NO_ENCONTRADO)
                else:
                    print(md.mostrar_camino(camino_lista=recorrido,
                                            tiempo=tiempo_total))
                    ca.crear_archivo_kml(
                        archivo_nombre, origen, origen, camino_lista=recorrido)
            except KeyError:
                print(RECORRIDO_NO_ENCONTRADO)

        elif comando == REDUCIR_CAMINOS:  # reducir_caminos destino.pj
            arbol = programa.arbol_tendido_minimo()
            print(md.mostrar_peso_total(arbol))
            ca.crear_archivo_pj(parametros[0], arbol)


if __name__ == '__main__':
    archivo = sys.argv[1]
    ejecutar(archivo)
