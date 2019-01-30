# corrigé examen prog

def creerFileVide():
	return []

def fileVide(f):
	return f == []

def enfiler(f, e):
	f.append(e)

def defiler(f):
	if fileVide(f):
		raise IndexError("attempt to remove element from empty queue")
	return f.pop(0)

def tete(f):
	if pileVide(f):
		raise IndexError("attempt to read head of empty queue")
	return f[0]



def creerPileVide():
	return []

def pileVide(p):
	return p == []

def empiler(p, e):
	p.append(e)

def depiler(p):
	if pileVide(p):
		raise IndexError("attempt to pop from empty stack")
	return p.pop()

def sommet(p):
	if pileVide(p):
		raise IndexError("attempt to read top of empty stack")
	return p[-1]

# besoin de conservation de l'ordre : set et dict à proscrire
# besoin de pouvoir modifier la structure : str et tuple à proscrire
# seule possibilité restante : list

# defiler(), tete(), depiler(), sommet() peuvent lever une exception (de type
# IndexError) si la file/pile est vide

if __name__ == '__main__':
	f = creerFileVide()
	for i in range(5):
		enfiler(f, i)
	while not fileVide(f):
		print(defiler(f))
	try:
		defiler(f)
	except Exception as e:
		print(e)
	try:
		print(tete(f))
	except Exception as e:
		print(e)

	p = creerPileVide()
	for i in range(5):
		empiler(p, i)
	while not pileVide(p):
		print(depiler(p))
	try:
		depiler(p)
	except Exception as e:
		print(e)
	try:
		print(sommet(p))
	except Exception as e:
		print(e)

