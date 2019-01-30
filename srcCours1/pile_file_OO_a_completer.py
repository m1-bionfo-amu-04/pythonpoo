class Pile:
	pass # a completer


class File:
	pass # a completer


if __name__ == "__main__": # ne pas toucher au code ci-dessous
	f = File()
	for i in range(5):
		f.enfiler(i)
	while not f.estVide():
		print(f.defiler())
	try:
		f.defiler()
	except IndexError as e:
		print(e)
	try:
		print(f.tete())
	except IndexError as e:
		print(e)

	p = Pile()
	for i in range(5):
		p.empiler(i)
	while not p.estVide():
		print(p.depiler())
	try:
		p.depiler()
	except IndexError as e:
		print(e)
	try:
		print(p.sommet())
	except IndexError as e:
		print(e)
