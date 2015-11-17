from tree import *
from IER import *
import time
import os

start_time = time.time()

listNames = ['Police_Stations', 'Edmonton_Catholic_Schools__2014_-_2015_', 'Edmonton_Public_Schools__2015_-_2016_', 'ETS_-_Bus_Stops_by_Landmarks', 'Playgrounds', 'Public_Libraries', 'Recreation_Centres', 'Fire_Stations']

tree = list()
for i in range(len(listNames)):
	t = Tree()
	t.createTree(listNames[i])
	tree.append(t)

re = pd.read_csv('realestate_refined.csv')
lat = re['PA_LATITUDE'].tolist()
lon = re['PA_LONGITUDE'].tolist()

f = open('realestate_facilities38.csv','w')
f.write(','.join(listNames) + '\n')

for j in range(len(lat)):
	for i in range(len(tree)):
		bestDist = IER( (lat[j],lon[j]), tree[i] )
		if(i < len(tree) -1):
			f.write(str(bestDist) + ',')
		else:
			f.write(str(bestDist) + '\n')
		
		#print 'Dist to closest', listNames[i], ':', bestDist
		
f.close()
print time.time() - start_time


