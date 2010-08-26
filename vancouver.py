#!/usr/bin/env python

import mapnik
m = mapnik.Map(3000,3000,"+proj=utm +zone=10 +datum=NAD83")
m.background = mapnik.Color('#000000')

s = mapnik.Style()
r=mapnik.Rule()
# r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#ffffff'),1.0))
s.rules.append(r)
m.append_style('My Style',s)

lyr = mapnik.Layer('world',"+proj=utm +zone=10 +datum=NAD83")
lyr.datasource = mapnik.Shapefile(file='./streets/public_streets.shp')
lyr.styles.append('My Style')

s2 = mapnik.Style()
r2=mapnik.Rule()
# r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r2.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#ffffff'),0.5))
s2.rules.append(r2)
m.append_style('My Style 2',s2)

ist = mapnik.Layer('world',"+proj=utm +zone=10 +datum=NAD83")
ist.datasource = mapnik.Shapefile(file='./contour/10-metre_contour_lines.shp')
ist.styles.append('My Style 2')

m.layers.append(lyr)
m.layers.append(ist)

# m.zoom_to_box(lyr.envelope())
mapnik.Coord(-122.99, 49.33), mapnik.Coord(-123.31, 49.18)
mapnik.render_to_file(m,'vancouver.png', 'png')

