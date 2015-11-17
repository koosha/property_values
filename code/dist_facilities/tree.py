import pandas as pd
from sklearn.neighbors import KDTree

class Tree:

	def __init__(self):
        	self.points = list()

	def createTree(self, name ):
		df = pd.read_csv(name +'.csv')
		lat = df['LATITUDE'].tolist()
		lon = df['LONGITUDE'].tolist()

		for i in range(len(lat)):
			self.points.append((lat[i], lon[i]))

		self.tree = KDTree(self.points, metric='euclidean')

		return self.tree


