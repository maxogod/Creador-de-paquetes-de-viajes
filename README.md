# Creador de paquetes de viajes

Este programa es para que dado un mapa de ciudades/paises posibles a visitar, y dadas
ciertas restricciones que el cliente imponga, se pueda crear automaticamente un plan de viaje
para este.

## Los 4 comandos:

~~~
ir <desde>, <hasta>, <nombre archivo a escribir .kml>
~~~
Encuentra el camino mas optimo entre las dos ubicaciones y lo muestra por pantalla asi como
guarda el recorrido en un archivo .kml que **puede ser visualizado en Google Earth**

~~~
itinerario <archivo obligatorio .csv>
~~~
A partir del archivo .csv pasado que debe contener que ciudades se quieren visitar primero que las otras
(podria ser un archivo con recomendaciones que le dieron al usuario) crea un itinerario y lo muestra por
pantalla

~~~
viaje < ubicacion origen>, <archivo .kml>
~~~
Crea un posible viaje desde ese origen que pase por todos lados del mapa dado, es especialmente
para aquellos usuarios que quieren explorar y pasear. Escribe un archivo .kml que **puede ser visualizado
en Google Earth**

~~~
reducir_caminos <nuevo mapa .pj>
~~~
Escribe un archivo .pj que contiene como ir a todas las ubicaciones en el menor tiempo posible,
esto solo muestra los caminos necesarios para llegar y que son los mas cortos.
Diferente al comando ir, este va a todos los puntos


## Como Correr:
~~~
1- Clonar el repositorio
2- Escribir lo siguiente en la terminal:
    python3 <path a paquetes_viajes.py> <path a su mapa.pj>
~~~

(ejemplos de los archivos usados en /archivos_tests y ejemplos de archivos de salida en /archivos_output)
