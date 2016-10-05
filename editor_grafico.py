def parsear_comando(comando):
    if comando == 'C':
        return {'comando': 'limpar', 'args': []}
    return {'comando': 'criar', 'args': [10, 10]}
