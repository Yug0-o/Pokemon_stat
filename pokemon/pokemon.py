from random import*
class Pokemon :
    def __init__(self, nom, energie, attaque, defense):
        self.n = nom
        self.E = energie
        self.A = attaque
        self.D = defense
        
    def __str__(self):
        return "{}-{}-{}-{}".format(self.n,self.E,self.A,self.D)
        
    def __add__(self,AD):

        de = randint(0,6)
        print("dé - ",de)
        
        if de%2 == 0:
            assaut = self.A + de
        else:
            assaut = self.A - de
            
        if assaut > AD.D:
            dommages = assaut - AD.D
            AD.E = AD.E - dommages
            print("domages - ",dommages)
            print(Pokemon1)
            print(Pokemon2)
 
import csv

chemin = str(input("veuillez renseigner le chemin du fichier csv: "))
CHEMINVERSFICHIER = chemin
f = open( CHEMINVERSFICHIER + "pokemon.csv", encoding="utf8") 
csv_reader = csv.reader(f,delimiter=';')

proba_1=randint(1,721)
proba_2=randint(1,721)

for row in csv_reader:
    if row[0] != "#" and int(row[0])==proba_1 :
        Pokemon1 = Pokemon(str(row[1]),int(row[5]),int(row[6]),int(row[7]))
    elif row[0] != "#" and int(row[0])==proba_2 :
        Pokemon2 = Pokemon(str(row[1]),int(row[5]),int(row[6]),int(row[7]))
   
for i in range (100):
    if i%2==0:
        if Pokemon2.E > 0 and Pokemon1.E > 0:
            print(Pokemon1 + Pokemon2)
        else :
            print("le combat est fini, le gagnant est ",Pokemon2.n)
            break
    else:
        if Pokemon2.E > 0 and Pokemon1.E > 0:
            print(Pokemon2 + Pokemon1)
        else :
            print("le combat est fini, le gagnant est ",Pokemon1.n)
            break

