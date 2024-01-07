from pendu import Pendu
import unittest

class TestPendu(unittest.TestCase):

    def test_retourne_string(self):
        jeu_pendu = Pendu()  # Créer une instance de la classe Pendu
        self.assertIsInstance(jeu_pendu.choisir_mot(), str)

    def test_retourne_string(self):
        jeu_pendu = Pendu()  # Créer une instance de la classe Pendu
        self.assertIsInstance(jeu_pendu.afficher_mot_masque(), str)

if __name__ == '__main__':
    unittest.main()