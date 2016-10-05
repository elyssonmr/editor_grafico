comandos = {
    'C': 'limpar',
    'I': 'criar',
    'L': 'colorir',
    'V': 'desenhar_seg_vertical'
}

matriz = []


def parsear_comando(comando):
    partes = comando.split()
    if partes[0] not in comandos.keys():
        return {'comando': '', 'args': []}

    comando_parseado = {}
    comando_parseado['comando'] = comandos[partes[0]]
    comando_parseado['args'] = partes[1:]
    return comando_parseado


def criar_matriz(linhas, colunas):
    linhas = int(linhas)
    colunas = int(colunas)
    for l in range(linhas):
        linha = ['O' for c in range(colunas)]
        matriz.append(linha)
