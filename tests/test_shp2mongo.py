import unittest
from shp2mongo import Shp2Mongo
from shapefile import ShapefileException
class TestShp2Mongo(unittest.TestCase):
    
    def setUp(self):
        self.shp2mongo = Shp2Mongo('tests/shapefiles/America_do_Sul')
    
    def test_is_shapefile(self):
        self.assertRaises(ShapefileException, Shp2Mongo, None)
    
    def test_fields_name(self):
        fields_name = self.shp2mongo.fields_name()
        self.assertIsInstance(fields_name, list)
    

if __name__ == '__main__':
    unittest.main()    
    
