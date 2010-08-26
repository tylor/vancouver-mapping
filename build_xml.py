#!/usr/bin/env python
import mapnik
mapfile = 'vancouver.xml'
map_output = 'vancouver_xml.png'
m = mapnik.Map(4000, 2800)
mapnik.load_map(m, mapfile)
# bbox = mapnik.Envelope(mapnik.Coord(-122.0, 55.0), mapnik.Coord(-130.0, 49.0))
bbox = mapnik.Envelope(mapnik.Coord(-123.10, 49.33), mapnik.Coord(-123.15, 49.18))
m.zoom_to_box(bbox) 
mapnik.render_to_file(m, map_output)

