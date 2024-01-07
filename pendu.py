import random

class Pendu:
    def choisir_mot(self):
        mots = [
            "chat", "soleil", "arbre", "maison", "fleur",
            "plage", "oiseau", "lune", "étoile", "route",
            "fraise", "montagne", "rivière", "pont", "pomme",
            "voiture", "école", "ballon", "livre", "nuage",
            "jardin", "arc-en-ciel", "café", "cœur", "chocolat",
            "cerise", "papillon", "nuage", "fenêtre", "porte",
            "poisson", "ciel", "chapeau", "chien", "chaton",
            "piano", "danse", "oiseau", "ballon", "forêt",
            "gâteau", "rue", "église", "vélo", "train",
            "avion", "bateau", "poème", "histoire", "musique",
            "amour", "bonheur", "rêve", "sourire", "rire",
            "pluie", "neige", "étoile filante", "hiver", "printemps",
            "été", "automne", "famille", "ami", "voyage",
            "sable", "pieds", "fenêtre", "porte", "ordinateur",
            "internet", "écran", "clavier", "souris", "table",
            "chaise", "lampe", "coussin", "couverture", "tapis",
            "cadeau", "carte", "lettre", "merci", "santé",
            "bonjour", "au revoir", "silence", "couleur", "joie",
            "tristesse", "douceur", "câlin", "bisou", "nuit",
            "jour", "moment", "instant", "tranquillité", "tendresse",
            "jouet", "musée", "photo", "parc", "rue",
            "manger", "boire", "dormir", "lire", "écrire",
            "dessiner", "jouer", "courir", "marcher", "écouter",
            "regarder", "sentir", "goûter", "aimer", "partager",
            "rêver", "penser", "espérer", "vivre", "grandir"
        ]
        return random.choice(mots)

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
        tentatives_restantes = 10

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