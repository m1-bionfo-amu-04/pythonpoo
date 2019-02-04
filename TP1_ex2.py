class Pile:
    def __init__(self):
        self.valeurs = []

    def empiler(self,e):
        self.valeurs.append(e)

    def estVide(self):
        return self.valeurs == []

    def depiler(self):
    	if self.estVide():
    		raise IndexError("attempt to pop from empty stack")
    	return self.valeurs.pop()

    def sommet(self):
    	if self.estVide():
    		raise IndexError("attempt to read top of empty stack")
    	return self.valeurs[-1]


class File:
    def __init__(self):
        self.valeurs = []

    def enfiler(self,e):
        self.valeurs.append(e)

    def estVide(self):
        return self.valeurs == []

    def defiler(self):
    	if self.estVide():
    		raise IndexError("attempt to pop from empty stack")
    	return self.valeurs.pop(0)

    def tete(self):
    	if self.estVide():
    		raise IndexError("attempt to read top of empty stack")
    	return self.valeurs[0]



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
