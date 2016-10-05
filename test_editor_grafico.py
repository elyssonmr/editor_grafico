import unittest

from editor_grafico import EditorGrafico


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


class ExecucaoComandoCriarMatrizTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    def test_cmd_criar_matriz(self):
        self.editor.criar_matriz('2', '2')

        esperado = [['O', 'O'], ['O', 'O']]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_limpar_matriz(self):
        self.editor.limpar_matriz()
        esperado = []

        self.assertEqual(esperado, self.editor.matriz)


class ExecucaoComandoAlteraMatriz(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()
        self.editor.criar_matriz('3', '3')

    def test_cmd_colorir_pixel(self):
        self.editor.colorir_pixel('1', '2', 'C')
        esperado = [
            ['O', 'C', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_segmento_vertical(self):
        self.editor.segmento_vertical('1', '2', '3', 'C')
        esperado = [
            ['O', 'C', 'C'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_segmento_horizontal(self):
        self.editor.segmento_horizontal('1', '3', '1', 'C')
        esperado = [
            ['C', 'O', 'O'],
            ['C', 'O', 'O'],
            ['C', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_retangulo(self):
        self.editor.desenhar_retangulo('1', '1', '3', '2', 'C')
        esperado = [
            ['C', 'C', 'O'],
            ['C', 'C', 'O'],
            ['C', 'C', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

if __name__ == "__main__":
    unittest.main()
