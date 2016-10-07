class EditorGrafico:
    def __init__(self):
        self.matriz = []
        self.comandos = {
            'C': self.limpar_matriz,
            'I': self.criar_matriz,
            'L': self.colorir_pixel,
            'V': self.segmento_vertical,
            'H': self.segmento_horizontal,
            'K': self.desenhar_retangulo,
            'F': self.preencher_regiao,
            'S': self.salvar_matriz,
            'X': self.encerrar_app,
            'D': self.dummy
        }

        self.sair = False

    def dummy(self):
        pass

    def parsear_comando(self, comando):
        partes = comando.split()
        if partes[0] not in self.comandos.keys():
            return {'comando': None, 'args': []}

        comando_parseado = {}
        comando_parseado['comando'] = self.comandos[partes[0]]
        comando_parseado['args'] = partes[1:]
        return comando_parseado

    def criar_matriz(self, colunas, linhas):
        self.linhas = int(linhas)
        self.colunas = int(colunas)
        for l in range(self.linhas):
            linha = ['O' for c in range(self.colunas)]
            self.matriz.append(linha)

    def limpar_matriz(self):
        self.matriz = []

    def colorir_pixel(self, coluna, linha, cor):
        linha = int(linha) - 1
        coluna = int(coluna) - 1
        self.matriz[linha][coluna] = cor

    def segmento_vertical(self, col, linha1, linha2, cor):
        col = int(col) - 1
        linha1 = int(linha1) - 1
        linha2 = int(linha2)
        for linha in range(linha1, linha2):
            self.matriz[linha][col] = cor

    def segmento_horizontal(self, col1, col2, linha, cor):
        col1 = int(col1) - 1
        col2 = int(col2)
        linha = int(linha) - 1

        for col in range(col1, col2):
            self.matriz[linha][col] = cor

    def desenhar_retangulo(self, x1, y1, x2, y2, cor):
        x1 = int(x1) - 1
        y1 = int(y1) - 1

        x2 = int(x2)
        y2 = int(y2)

        for x in range(x1, x2):
            for y in range(y1, y2):
                self.matriz[x][y] = cor

    def fora_matriz(self, x, y):
        if x < 0 or y < 0:
            return True

        if x >= self.linhas or y >= self.colunas:
            return True

        return False

    def buscar_proximos(self, x, y, cor):
        proximos = set()
        for xdes in range(x - 1, x + 2):
            for ydes in range(y - 1, y + 2):
                if not self.fora_matriz(xdes, ydes):
                    if (xdes != x or ydes != y):
                        if self.matriz[xdes][ydes] == cor:
                            proximos.add((xdes, ydes))
        return proximos

    def preencher_regiao(self, x, y, cor):
        x = int(x)
        y = int(y)
        cor_item = self.matriz[x][y]

        proximos = set()
        proximos.add((x, y))

        while len(proximos) > 0:
            px, py = proximos.pop()
            proximos.update(self.buscar_proximos(px, py, cor_item))
            self.matriz[px][py] = cor

    def salvar_matriz(self, nome_arquivo):
        print(nome_arquivo)
        arquivo = open(nome_arquivo, 'w')
        linhas = []
        for x in range(0, self.linhas):
            linha = ''
            for y in range(0, self.colunas):
                linha += self.matriz[x][y]
            linhas.append(linha)
        arquivo.write('\n'.join(linhas))
        arquivo.flush()
        arquivo.close()
        print('\n'.join(linhas))

    def encerrar_app(self):
        self.sair = True

    def ler_input(self):
        return input()

    def ler_comando(self):
        entrada = self.ler_input()
        return self.parsear_comando(entrada)

    def main_loop(self):
        while not self.sair:
            comando = self.ler_comando()

            if comando['comando']:
                comando['comando'](*comando['args'])


def main():
    editor = EditorGrafico()
    editor.main_loop()

if __name__ == '__main__':
    main()
