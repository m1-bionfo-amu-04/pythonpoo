from point import Point


class Rectangle:
	def __init__(self, x1, y1, x2, y2):
		self.so = Point(x1, y1)
		self.ne = Point(x2, y2)

	def aire(self):
		largeur = self.ne.x() - self.so.x()
		hauteur = self.ne.y() - self.so.y()
		return abs(largeur * hauteur)

	def __str__(self):
		return str(self.so) + '@' + str(self.ne)

if __name__ == '__main__':
	a = Rectangle(1, 2, 3, 4)
	print('a:', a)
	print('aire:', a.aire())
