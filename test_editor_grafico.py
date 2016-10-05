import unittest

from editor_grafico import criar_matriz, matriz, EditorGrafico


class PasearComandoTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    def test_parse_cmd_criar_matriz(self):
        cmd_criar = "I 10 10"
        esperado = {'comando': 'criar', 'args': ['10', '10']}
        resp = self.editor.parsear_comando(cmd_criar)

        self.assertEqual(esperado, resp)

    def test_parse_cmd_limpar_matriz(self):
        cmd_limpar = "C"
        esperado = {'comando': 'limpar', 'args': []}
        resp = self.editor.parsear_comando(cmd_limpar)

        self.assertEqual(esperado, resp)

    def test_parse_cmd_colorir_pixel(self):
        cmd_colorir = "L 10 1 C"
        esperado = {'comando': "colorir", 'args': ['10', '1', 'C']}
        resp = self.editor.parsear_comando(cmd_colorir)

        self.assertEqual(esperado, resp)

    def test_parse_cmd_desenhar_seg_vertical(self):
        cmd_desenhar_segmento = "V 10 1 2 C"
        esperado = {
            'comando': 'desenhar_seg_vertical',
            'args': ['10', '1', '2', 'C']
        }
        resp = self.editor.parsear_comando(cmd_desenhar_segmento)

        self.assertEqual(esperado, resp)

    def test_parse_cmd_diferente(self):
        cmd_diferente = "T"
        esperado = {'comando': '', 'args': []}
        resp = self.editor.parsear_comando(cmd_diferente)

        self.assertEqual(esperado, resp)


class ExecucaoComandoTestCase(unittest.TestCase):
    def test_cmd_criar_matriz(self):
        criar_matriz('2', '2')

        esperado = [['O', 'O'], ['O', 'O']]

        self.assertEqual(esperado, matriz)


if __name__ == "__main__":
    unittest.main()
