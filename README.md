This repository contains configuration files used to create a nice Vancouver map using Open Data and Mapnik. Here is what vancouver-light-compiled.xml looks like: http://twitpic.com/2xqcrq

![Picture of a Vancouver
tileset](https://github.com/tylor/vancouver-mapping/raw/master/vancouver-light-compiled.png)

Recomended tools:

* Mapnik
* Quantum GIS (with Quantumnik plugin)
* Cascadenik
* TileLite

To compile and run:

* Compile with Cascadenik: cascadenik-compile.py vancouver-light.mml > vancouver-light-compiled.xml
* Run with TileLite: liteserv.py -b 2048 vancouver-light-compiled.xml
* Open map.html in a browser and it will connect to TileLite and show your tiles!

Data used:

* Local area boundary data: http://data.vancouver.ca/datacatalogue/localAreaBoundary.htm
* Building Footprints 1999: http://data.vancouver.ca/datacatalogue/buildingFootprint1999.htm
* Parks (polygon features): http://data.vancouver.ca/datacatalogue/parks.htm
* City streets package: http://data.vancouver.ca/datacatalogue/cityStreets.htm

Summary of files:

* 9x9\_transparent.png - a 9x9 pixel PNG to create a diagonal stripe
* map.html - basic OpenLayers map page centered on Vancouver and set to load tiles from TileLite at http://localhost:8000
* vancouver-dark.qgs - Quantum GIS file with a couple layers and styles
* vancouver-dark.xml - Mapnik XML file generated by Quantumnik from within Quantum GIS
* vancouver-light.xml - Mapnik XML file generated by Quantumnik from within Quantum GIS
* vancouver-light.mml - Cascadenik layers file which sets map info, stylesheet to use, and layer precedence.
* vancouver-light.mss - Cascadenik stylesheet with some basic styles
* vancouver-light-compiled.xml - Mapnik XML file compiled from vancouver-light.mml using Cascadenik
