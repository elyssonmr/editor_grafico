import unittest
import sys
import os
from io import StringIO

from editor_grafico import EditorGrafico


class PasearComandoTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    def test_parse_cmds(self):
        comandos = [
            'I 10 10',
            'C',
            'L 1 1 C',
            'V 1 1 3 C',
            'H 2 4 1 C',
            'K 1 2 3 5 C',
            'F 2 4 C',
            'S arq.bmp',
            'X'
        ]
        esperados = [
            {'comando': self.editor.criar_matriz,
             'args': ['10', '10']},
            {'comando': self.editor.limpar_matriz,
             'args': []},
            {'comando': self.editor.colorir_pixel,
             'args': ['1', '1', 'C']},
            {'comando': self.editor.segmento_vertical,
             'args': ['1', '1', '3', 'C']},
            {'comando': self.editor.segmento_horizontal,
             'args': ['2', '4', '1', 'C']},
            {'comando': self.editor.desenhar_retangulo,
             'args': ['1', '2', '3', '5', 'C']},
            {'comando': self.editor.preencher_regiao,
             'args': ['2', '4', 'C']},
            {'comando': self.editor.salvar_matriz,
             'args': ['arq.bmp']},
            {'comando': self.editor.encerrar_app,
             'args': []},
        ]

        for comando, esperado in zip(comandos, esperados):
            resp = self.editor.parsear_comando(comando)
            self.assertEqual(esperado, resp)


class ExecucaoComandoCriarMatrizTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    def test_cmd_criar_matriz(self):
        self.editor.criar_matriz('2', '2')

        esperado = [['O', 'O'], ['O', 'O']]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_limpar_matriz(self):
        self.editor.matriz = [['O', 'O'], ['O', 'O']]
        self.editor.limpar_matriz()
        esperado = []

        self.assertEqual(esperado, self.editor.matriz)


class ExecucaoComandosAlterarMatriz(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()
        self.editor.criar_matriz('3', '3')

    def test_cmd_colorir_pixel(self):
        self.editor.colorir_pixel('1', '2', 'C')
        esperado = [
            ['O', 'O', 'O'],
            ['C', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_segmento_vertical(self):
        self.editor.segmento_vertical('1', '2', '3', 'C')
        esperado = [
            ['O', 'O', 'O'],
            ['C', 'O', 'O'],
            ['C', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_segmento_horizontal(self):
        self.editor.segmento_horizontal('1', '3', '1', 'C')
        esperado = [
            ['C', 'C', 'C'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_cmd_retangulo(self):
        self.editor.desenhar_retangulo('1', '1', '2', '3', 'C')
        esperado = [
            ['C', 'C', 'O'],
            ['C', 'C', 'O'],
            ['C', 'C', 'O']
        ]

        self.assertEqual(esperado, self.editor.matriz)

    def test_encerrar_programa(self):
        self.editor.encerrar_app()
        self.assertTrue(self.editor.sair)


class PreencherRegiaoTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()
        self.editor.criar_matriz('3', '3')
        self.editor.matriz = [
            ['B', 'B', 'O'],
            ['O', 'B', 'B'],
            ['O', 'O', 'O']
        ]

    def test_buscar_proximos(self):
        esperado = set([(0, 1), (1, 1)])
        resp = self.editor.buscar_proximos(0, 0, 'B')

        self.assertEqual(esperado, resp)

    def test_preencher_regiao(self):
        esperado = [
            ['C', 'C', 'O'],
            ['O', 'C', 'C'],
            ['O', 'O', 'O']
        ]
        self.editor.preencher_regiao('1', '1', 'C')

        self.assertEqual(esperado, self.editor.matriz)


class SalvarArquivoTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()
        self.editor.criar_matriz('3', '3')
        self.nome_arquivo = 'teste.bmp'
        sys.stdout = StringIO()

    def test_cmd_salvar_matriz(self):
        self.editor.salvar_matriz(self.nome_arquivo)

        esperado = 'OOO\nOOO\nOOO'
        arquivo = open(self.nome_arquivo, 'r')
        conteudo = arquivo.read()
        arquivo.close()

        self.assertEqual(esperado, conteudo)

    def tearDown(self):
        if os.path.exists(self.nome_arquivo):
            os.remove(self.nome_arquivo)
