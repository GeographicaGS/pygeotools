import json

class NumpytoGeo(object):
	
	def __init__(self,npdata):
		self.npdata = npdata

	def toGeoJSONDict(self,coordinates,properties):
  	
		geojson = {
			"type": "FeatureCollection",
			"features": []
		}

		for i in range(self.npdata.shape[1]):
			for j in range(self.npdata.shape[2]):

				p = {}

				for n,v in properties.iteritems():
					p[n] = self.npdata[v][i][j]

				geojson["features"].append({
					"type": "Feature",
					"geometry": {
						"type": "Point",
						"coordinates": [self.npdata[coordinates["x"]][i][j],self.npdata[coordinates["y"]][i][j]]
					},
					"properties": p
				})

		return geojson

	def toGeoJSONFile(self,coordinates,properties,filename):
		geojson = self.toGeoJSONDict(coordinates,properties)
		with open(filename, 'w') as fp:
			json.dump(geojson, fp)

