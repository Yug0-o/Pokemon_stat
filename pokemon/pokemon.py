from random import randint, choice
import csv

# Classe Pokemon
class Pokemon:
    """
    Classe contenant les stats du Pokémon, l'affichage des stats et la mécanique d'attaque.
    """
    def __init__(self, nom, energie, attaque, defense):
        self.nom = nom
        self.energie = energie
        self.attaque = attaque
        self.defense = defense

    def __str__(self):
        return "{}-{}-{}-{}".format(self.nom, self.energie, self.attaque, self.defense)

    def attaquer(self, adversaire):
        de = randint(0, 6)
        print("dé - ", de)
        
        assaut = self.attaque + de if de % 2 == 0 else self.attaque - de
        if assaut > adversaire.defense:
            dommages = assaut - adversaire.defense
            adversaire.energie -= dommages
            print("dommages - ", dommages)
 
# Fonction pour lire les Pokémon depuis un fichier CSV
def lire_pokemons(chemin_fichier):
    """
    Lit un fichier et crée les Pokémon à partir du CSV.
    Param : Le chemin vers le fichier.
    Return : Une liste contenant tous les Pokémon.
    """
    pokemons = []
    with open(chemin_fichier, encoding="utf8") as f:
        csv_reader = csv.reader(f, delimiter=';')
        for row in csv_reader:
            if row[0] != "#" and row[0].isdigit():
                pokemons.append(Pokemon(row[1], int(row[5]), int(row[6]), int(row[7])))
    return pokemons

# Fonction pour simuler un combat entre deux Pokémon
def combat(pokemon1, pokemon2):
    """
    Simule le combat et annonce le vainqueur.
    Param : Les deux Pokémon (objets).
    Return : None.
    """
    for i in range(100):
        if pokemon1.energie <= 0 or pokemon2.energie <= 0:
            break
        attaquant = pokemon1 if i % 2 == 0 else pokemon2
        defenseur = pokemon2 if i % 2 == 0 else pokemon1
        attaquant.attaquer(defenseur)

    gagnant = pokemon1.nom if pokemon1.energie > 0 else pokemon2.nom
    print("Le combat est fini, le gagnant est", gagnant)


# Lecture du fichier et création des Pokémon
chemin = input("Veuillez renseigner le chemin du fichier csv: ")
pokemons = lire_pokemons(chemin + "pokemon.csv")

# Choix des deux Pokémon
pokemon1 = choice(pokemons)
pokemon2 = choice(pokemons)
while pokemon1 == pokemon2:  # Empêche que les Pokémon soient les mêmes
    pokemon2 = choice(pokemons)

# Combat
combat(pokemon1, pokemon2)