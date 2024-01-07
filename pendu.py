import random
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

class Pendu:
    def choisir_mot(self):
        noms_communs = list(set(wordnet.words()))
        return random.choice(noms_communs)

    def afficher_mot_masque(self, mot, lettres_trouvees):
        mot_masque = ""
        for lettre in mot:
            if lettre in lettres_trouvees:
                mot_masque += lettre
            else:
                mot_masque += "_"
        return mot_masque

    def pendu(self):
        mot_secret = self.choisir_mot()
        lettres_trouvees = []
        tentatives_restantes = 7

        print("Bienvenue au jeu du pendu!")
        print("Mot actuel :", self.afficher_mot_masque(mot_secret, lettres_trouvees))

        while tentatives_restantes > 0 and "_" in self.afficher_mot_masque(mot_secret, lettres_trouvees):
            lettre = input("Devinez une lettre : ").lower()

            if lettre in lettres_trouvees:
                print("Vous avez déjà deviné cette lettre. Essayez une autre.")
                continue

            lettres_trouvees.append(lettre)

            if lettre in mot_secret:
                print("Bonne devinette !")
            else:
                print("Mauvaise devinette.")
                tentatives_restantes -= 1

            print("Mot actuel :", self.afficher_mot_masque(mot_secret, lettres_trouvees))
            print("Lettres déjà devinées :", ", ".join(lettres_trouvees))
            print("Tentatives restantes :", tentatives_restantes)

        if "_" not in self.afficher_mot_masque(mot_secret, lettres_trouvees):
            print("Félicitations ! Vous avez deviné le mot :", mot_secret)
        else:
            print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était :", mot_secret)

# Appel de la fonction pour démarrer le jeu
jeu_pendu = Pendu()
jeu_pendu.pendu()