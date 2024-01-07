from pendu import Pendu
import unittest

class TestPendu(unittest.TestCase):

    def test_return_string(self):
        jeu_pendu = Pendu()  # Créer une instance de la classe Pendu
        print(jeu_pendu.choisir_mot())

if __name__ == '__main__':
    unittest.main()