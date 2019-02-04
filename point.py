#!/usr/bin/python3
# -*- coding: utf-8 -*-

# avec les coordonnées CARTESIENNES

import math

class Point:
	''' class representing a point in 2-dimensions'''

	def __init__(self, x = 0, y = 0):
		'''construct a point from cartesian coordinates x,y'''
		self.placement(x, y)

	def __eq__(self, autrePoint):
		return isinstance(autrePoint, Point) \
			and	self.x() == autrePoint.x() \
			and	self.y() == autrePoint.y()

	def __repr__(self):
		return "Point(x=" + str(self.__x) + ", y=" + str(self.__y) + ")"

	def __str__(self):
		'''return cartesian coordinates of point'''
		return "(" + str(self.__x) + ", " + str(self.__y) + ")"

	def x(self): return self.__x

	def y(self): return self.__y

	def r(self): return math.sqrt(self.__x ** 2 + self.__y ** 2)

	def t(self): return math.atan2(self.__y, self.__x)

	def distance(self, p):
		'''return Euclidian distance between 2 self and other Point'''
		return math.sqrt((self.__x - p.x())**2 + (self.__y - p.y())**2)

	def placement(self, x, y):
		'''sets the point at coordinates x, y
		   raise ValueError if x or y is negative'''
		if x < 0 or y < 0:
			raise ValueError('Bad value: coordinates must be positive')
		self.__x = x
		self.__y = y

	def homothetie(self, k):
		self.__x = self.__x * k
		self.__y = self.__y * k

	def translation(self, dx, dy):
		self.__x = self.__x + dx
		self.__y = self.__y + dy

	def rotation(self, a):
		coord_r = self.r()
		coord_t = self.t() + a
		self.__x = coord_r * math.cos(coord_t)
		self.__y = coord_r * math.sin(coord_t)

class LignePol:
	def __init__(self,sommets):
		self.__sommets = sommets
		self.__nbSommets = len(sommets)

	def getSommet(self,i):
		return self.__sommets[i]

	def setSommet(self,i,p):
		self.__sommets[i] = p

	def __str__(self):
		liste = ""
		for i in range(self.__nbSommets):
			liste += str(self.__sommets[i]) + " , "
		return liste

	def homothetie(self,k):
		for i in range(self.__nbSommets):
			self.setSommet(i,self.getSommet(i).homothetie(k))

	def translation(self,dx,dy):
		for i in range(self.__nbSommets):
			self.setSommet(i,self.getSommet(i).translation(dx,dy))

	def rotation(self,a):
		for i in range(self.__nbSommets):
			self.setSommet(i,self.getSommet(i).rotation(a))


if __name__=='__main__':
	p = Point(3, 4)
	p2 = "point"
	p3 = Point(3, 4)
	p4 = Point(4, 4)
	print(p==p, not p==p2, p==p3, not p==p4) # T T T T
	print(p) # (3, 4)
	p.homothetie(3.0)
	print(p) # (9, 12)
	p.translation(1, 1)
	print(p) # (10, 13)
	p.rotation(math.pi/2)
	print(p) # (-13, 10)
	print(p3.distance(p4)) # 1
	print(repr(p))
