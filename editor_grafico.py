comandos = {
    'C': 'limpar',
    'I': 'criar',
    'L': 'colorir',
    'V': 'desenhar_seg_vertical'
}


def parsear_comando(comando):
    partes = comando.split()
    if partes[0] not in comandos.keys():
        return {'comando': '', 'args': []}

    comando_parseado = {}
    comando_parseado['comando'] = comandos[partes[0]]
    comando_parseado['args'] = partes[1:]
    return comando_parseado
