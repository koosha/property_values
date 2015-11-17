import kdtree
from LatLon import *
import googlemaps
import time

gmaps = googlemaps.Client(key='AIzaSyCy')

def IER( point, kdt ):

	tree = kdt.tree
	points = kdt.points
	p = LatLon(point[0], point[1])

	dist, ind = tree.query([point], k=1)
	ix = ind[0][0]

	p2 = points[ix]
	distance = gmaps.distance_matrix(point, p2, mode="driving")
	netDistance = distance["rows"][0]["elements"][0]["distance"]["value"]
	bestDistance = netDistance

	i = 1
	dist, ind = tree.query([point], k = i+1)
	ix = ind[0][i]
	pe = points[ix]
	nnPoint = LatLon(pe[0], pe[1])
	euclideanDistance = p.distance(nnPoint)*1000

	while (euclideanDistance < bestDistance):
		p2 = (pe[0], pe[1])
		distance = gmaps.distance_matrix(point, p2, mode="driving")
		netDistance = distance["rows"][0]["elements"][0]["distance"]["value"]
		if (netDistance < bestDistance):
			bestDistance = netDistance

		i = i+1
		dist, ind = tree.query([point], k = i+1)
		ix = ind[0][i]
		pe = points[ix]
		nnPoint = LatLon(pe[0], pe[1])
		lastED = euclideanDistance
		euclideanDistance = p.distance(nnPoint)*1000

		while (lastED == euclideanDistance):
			i = i+1
			dist, ind = tree.query([point], k = i+1)
			ix = ind[0][i]
			pe = points[ix]
			nnPoint = LatLon(pe[0], pe[1])
			lastED = euclideanDistance
			euclideanDistance = p.distance(nnPoint)*1000

	return bestDistance
		
