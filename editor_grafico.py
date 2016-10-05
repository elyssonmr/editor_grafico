comandos = {'C': 'limpar', 'I': 'criar', 'L': 'colorir'}


def parsear_comando(comando):
    partes = comando.split()
    comando_parseado = {}
    comando_parseado['comando'] = comandos[partes[0]]
    comando_parseado['args'] = partes[1:]
    return comando_parseado
