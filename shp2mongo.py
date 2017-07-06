import shapefile
import sys
import json

class Shp2GeoJSON(object):

    def __init__(self, shp_file):
        self.shp = shapefile.Reader(shp_file)

    def geojson(self):
        features = []
        for sr in self.shp.shapeRecords():
            properties = dict(zip(self.fields_name(), sr.record))
            geom = sr.shape.__geo_interface__
            features.append(dict(type="Feature",  geometry=geom, properties=properties))
        return dict(type="FeatureCollection", features=features)
    
    def fields_name(self):
        fields = self.shp.fields
        return [f[0] for f in fields[1:]]

    def dump_geojson(self):
        return json.dumps(self.geojson())



class Shp2Mongo(Shp2GeoJSON):

    def __init__(self, shp_file):
        super(Shp2Mongo, self).__init__(shp_file)     

    def dump_mongoimport(self):
        features = self.geojson()
        return '\n'.join(json.dumps(feature) for feature in features['features'])

    
