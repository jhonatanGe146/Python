#ModuleNotFoundError: se produce cuando se intenta importar un módulo que no existe o que no se puede encontrar.
def ErrordeModulo():
    try:
        import ramdom
    except ModuleNotFoundError:
        print("ModuleNotFoundError: Módulo no encontrado")

ErrordeModulo()