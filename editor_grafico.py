class EditorGrafico:
    def __init__(self):
        self.matriz = []
        self.comandos = {
            'C': 'limpar',
            'I': 'criar',
            'L': 'colorir',
            'V': 'desenhar_seg_vertical'
        }

    def parsear_comando(self, comando):
        partes = comando.split()
        if partes[0] not in self.comandos.keys():
            return {'comando': '', 'args': []}

        comando_parseado = {}
        comando_parseado['comando'] = self.comandos[partes[0]]
        comando_parseado['args'] = partes[1:]
        return comando_parseado

    def criar_matriz(self, linhas, colunas):
        self.linhas = int(linhas)
        self.colunas = int(colunas)
        for l in range(self.linhas):
            linha = ['O' for c in range(self.colunas)]
            self.matriz.append(linha)

    def limpar_matriz(self):
        self.matriz = []

    def colorir_pixel(self, x, y, cor):
        x = int(x) - 1
        y = int(y) - 1
        self.matriz[x][y] = cor

    def segmento_vertical(self, x, y1, y2, cor):
        x = int(x) - 1
        y1 = int(y1) - 1
        y2 = int(y2)
        for y in range(y1, y2):
            self.matriz[x][y] = cor

    def segmento_horizontal(self, x1, x2, y, cor):
        x1 = int(x1) - 1
        x2 = int(x2)
        y = int(y) - 1

        for x in range(x1, x2):
            self.matriz[x][y] = cor

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

        if x > self.linhas or y > self.colunas:
            return True

        return False

    def buscar_proximos(self, x, y, cor):
        proximos = set()
        for xdes in range(x - 1, x + 2):
            for ydes in range(x - 1, x + 2):
                if not self.fora_matriz(xdes, ydes):
                    if (xdes != x or ydes != y):
                        if self.matriz[xdes][ydes] == cor:
                            proximos.add((xdes, ydes))
        return proximos
