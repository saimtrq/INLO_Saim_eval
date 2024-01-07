from pendu import Pendu
import unittest

class TestPendu(unittest.TestCase):

    def test_retourne_string(self):
        jeu_pendu = Pendu()
        self.assertIsInstance(jeu_pendu.choisir_mot(), str)

    def test_affiche_t__t(self):
        jeu_pendu = Pendu()
        lettre_trouvé = ['a', 't', 'c']
        self.assertEqual(jeu_pendu.afficher_mot_masque('test', lettre_trouvé), 't__t')

if __name__ == '__main__':
    unittest.main()