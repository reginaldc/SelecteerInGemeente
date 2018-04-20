from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
import processing
#script gaat er van uit dat de laag gemeentegrens aanwezig is

print("Dit script maakt shapefiles aan in C:\temp van de features die binnen het grondgebied van Ingelmunster vallen")
for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
    if lyr.name() == "gemeentegrens":
        layer = lyr
        break
# Get the first feature from the layer
feature = layer.getFeatures().next()
# fetch geometry
geom = QgsGeometry(feature.constGeometry())

layers = iface.legendInterface().layers()

for lyr in layers:
    ids = []
    aanwezig = 0
    print(lyr.name())
    for feat in lyr.getFeatures():
        if feat.geometry().intersects(geom):
            aanwezig = 1
            #add feature to shapefile with the name of the layer and Ingelmunster appended
            ids.append(feat.id())
    lyr.setSelectedFeatures(ids)
    if aanwezig == 1:
        QgsVectorFileWriter.writeAsVectorFormat( lyr, 'C:/temp/' + lyr.name() + "Ingelmunster.shp", "utf-8", layer.crs(), "ESRI Shapefile", 1)

print("done")

         
    