# Tour Package Creator

This program automatically generates a Tour Package given a map of possible cities/countries to visit and certain restrictions
made by the client.

## The 4 commands:

~~~
ir <desde>, <hasta>, <nombre archivo a escribir .kml>
~~~
Finds the most optimal path between two points and shows it on the screen, as well as it saves
the path in a .kml file **which can be visualized on Google Earth** 

~~~
itinerario <archivo obligatorio .csv>
~~~
Generates and shows to the user a schedule built from a .csv file which contains information about which location they want to
see first. (It could be a file with recommendations someone gave to the user)

~~~
viaje < ubicacion origen>, <archivo .kml>
~~~
Generates a possible trip that starts in the given origin, and goes through every single location and route, specially for those
who want to explore and enjoy. Saves a .kml file **which can be visualized on Google Earth** 

~~~
reducir_caminos <nuevo mapa .pj>
~~~
Writes a .pj file containing a roadmap to every location in the least possible time.
It only shows the necessary and shortest routes.

## How To Run:
~~~
1- Clone the repository
2- Type the following in the terminal:
    python3 <path to paquetes_viajes.py> <path to su mapa.pj>
~~~

(examples of used files in /archivos_tests and examples of the output files in /archivos_output)
