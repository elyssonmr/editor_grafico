import unittest

from editor_grafico import parsear_comando


class PasearComandoTestCase(unittest.TestCase):
    def test_parse_comando_criar_matriz(self):
        comando_criar = "I 10 10"
        esperado = {'comando': 'criar', 'args': [10, 10]}
        resp = parsear_comando(comando_criar)

        self.assertEqual(esperado, resp)

    def test_parse_comando_limpa_matriz(self):
        comando_limpar = "C"
        esperado = {'comando': 'limpar', 'args': []}
        resp = parsear_comando(comando_limpar)

        self.assertEqual(esperado, resp)


if __name__ == "__main__":
    unittest.main()
