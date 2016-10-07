import unittest
from unittest.mock import patch
import os
import subprocess

from editor_grafico import EditorGrafico


class MainLoopTestCase(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    @patch('test_editor_grafico.EditorGrafico.ler_input')
    def test_ler_comando_criar_matriz(self, _ler_input):
        _ler_input.return_value = 'I 3 3'
        esperado = {'comando': self.editor.criar_matriz, 'args': ['3', '3']}

        resp = self.editor.ler_comando()

        _ler_input.assert_called_once_with()

        self.assertEqual(esperado, resp)

    @patch('test_editor_grafico.EditorGrafico.ler_input')
    def test_ler_comando_invalido(self, _ler_input):
        _ler_input.return_value = 'Q A B'
        esperado = {'comando': None, 'args': []}

        resp = self.editor.ler_comando()

        self.assertEqual(esperado, resp)

    @patch('test_editor_grafico.EditorGrafico.ler_comando')
    def test_main_loop_with_command_create(self, _ler_comando):
        _ler_comando.side_effect = [
            {'comando': self.editor.criar_matriz, 'args': ['3', '3']},
            {'comando': self.editor.encerrar_app, 'args': []}
        ]
        esperado = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]
        self.editor.main_loop()

        self.assertEqual(esperado, self.editor.matriz)

    @patch('test_editor_grafico.EditorGrafico.ler_comando')
    def test_main_loop_criar_colorir(self, _ler_input):
        _ler_input.side_effect = [
            {'comando': self.editor.criar_matriz, 'args': ['3', '3']},
            {'comando': self.editor.colorir_pixel, 'args': ['1', '1', 'C']},
            {'comando': self.editor.encerrar_app, 'args': []}
        ]

        esperado = [
            ['C', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.editor.main_loop()

        self.assertEqual(esperado, self.editor.matriz)

    @patch('test_editor_grafico.EditorGrafico.ler_comando')
    def test_main_loop_criar_invalido(self, _ler_input):
        _ler_input.side_effect = [
            {'comando': self.editor.criar_matriz, 'args': ['3', '3']},
            {'comando': None, 'args': []},
            {'comando': self.editor.encerrar_app, 'args': []}
        ]

        esperado = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.editor.main_loop()

        self.assertEqual(esperado, self.editor.matriz)


class SimulacaoProcessoTestCase(unittest.TestCase):
    def test_01(self):
        p = subprocess.Popen(
            ['python3', 'editor_grafico.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        input_comandos = b'I 5 6\nL 2 3 A\nS one.bmp\nG 2 3 J\nV 2 3 4 W\n' + \
            b'H 3 4 2 Z\nF 3 3 J\nS two.bmp\nX\n'

        esperado = 'one.bmp\nOOOOO\nOOOOO\nOAOOO\nOOOOO\nOOOOO\nOOOOO\n' + \
            'two.bmp\nJJJJJ\nJJZZJ\nJWJJJ\nJWJJJ\nJJJJJ\nJJJJJ\n'

        output = p.communicate(input=input_comandos)[0]

        self.assertEqual(esperado, output.decode('utf-8'))

    def test_02(self):
        p = subprocess.Popen(
            ['python3', 'editor_grafico.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        input_comandos = b'I 10 9\nL 5 3 A\nG 2 3 J\nV 2 3 4 W\n' + \
            b'H 1 10 5 Z\nF 3 3 J\nK 2 7 8 8 E\nF 9 9 R\nS one.bmp\nX\n'

        esperado = 'one.bmp\nJJJJJJJJJJ\nJJJJJJJJJJ\nJWJJAJJJJJ\n' + \
            'JWJJJJJJJJ\nZZZZZZZZZZ\nRRRRRRRRRR\nREEEEEEERR\nREEEEEEERR\n' + \
            'RRRRRRRRRR\n'

        output = p.communicate(input=input_comandos)[0]

        self.assertEqual(esperado, output.decode('utf-8'))

    def tearDown(self):
        for f in os.listdir('.'):
            if f.endswith('.bmp'):
                os.remove(f)
