import unittest

from editor_grafico import parsear_comando


class PasearComandoTestCase(unittest.TestCase):
    def test_parse_comando_criar_matriz(self):
        comando_criar = "I 10 10"
        esperado = {'comando': 'criar', 'args': ['10', '10']}
        resp = parsear_comando(comando_criar)

        self.assertEqual(esperado, resp)

    def test_parse_comando_limpa_matriz(self):
        comando_limpar = "C"
        esperado = {'comando': 'limpar', 'args': []}
        resp = parsear_comando(comando_limpar)

        self.assertEqual(esperado, resp)

    def test_parse_comando_colorir_pixel(self):
        comando_colorir = "L 10 1 C"
        esperado = {'comando': "colorir", 'args': ['10', '1', 'C']}
        resp = parsear_comando(comando_colorir)

        self.assertEqual(esperado, resp)

    def test_parse_comando_desenhar_seg_vertical(self):
        comando_desenhar_segmento = "V 10 1 2 C"
        esperado = {
            'comando': 'desenhar_seg_vertical',
            'args': ['10', '1', '2', 'C']
        }
        resp = parsear_comando(comando_desenhar_segmento)

        self.assertEqual(esperado, resp)


if __name__ == "__main__":
    unittest.main()
