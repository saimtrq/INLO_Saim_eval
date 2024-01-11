from pendu import Pendu
import unittest

class TestPendu(unittest.TestCase):

    def test_retourne_string(self):
        jeu_pendu = Pendu()
        self.assertIsInstance(jeu_pendu.choisir_mot(), str)


    def test_lettre_existe_mot(self):
        jeu_pendu = Pendu()
        lettre_a_trouver = "s"
        mot_secret = "soleil"
        self.assertTrue(jeu_pendu.existe_lettre(lettre_a_trouver, mot_secret))

    def test_retourne_t__t(self):
        jeu_pendu = Pendu()
        lettre_trouvé = ['a', 't', 'c']
        self.assertEqual(jeu_pendu.afficher_mot_masque('test', lettre_trouvé), 't__t')


    def test_retourne_carr____r__(self):
        jeu_pendu = Pendu()
        lettre_trouvé = ['a', 'r', 'c']
        self.assertEqual(jeu_pendu.afficher_mot_masque('carrosserie', lettre_trouvé), 'carr____r__')

    def test_retourne_carr____r__(self):
        jeu_pendu = Pendu()
        lettre_trouvé = ['a', 'r', 'c']
        self.assertEqual(jeu_pendu.afficher_mot_masque('carrosserie', lettre_trouvé), 'carr____r__')

if __name__ == '__main__':
    unittest.main()