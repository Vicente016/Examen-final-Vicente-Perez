def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1, 2, 3, 4, 5, 6):
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")


def cupos_genero(genero, peliculas, cartelera):
    total = 0
    for codigo in peliculas:
        datos = peliculas[codigo]
        if datos[1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print("El total de cupos disponibles es:", total)


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(titulo + "--" + codigo)
    resultados.sort()
    if len(resultados) == 0:
        print("No hay peliculas en ese rango de precios")
    else:
        print("Las peliculas encontradas son:", resultados)


def buscar_codigo(codigo, cartelera):
    for c in cartelera:
        if c.lower() == codigo.lower():
            return True
    return False


def actualizar_precio(codigo, nuevo_precio, cartelera):
    if buscar_codigo(codigo, cartelera):
        for c in cartelera:
            if c.lower() == codigo.lower():
                cartelera[c][0] = nuevo_precio
                return True
    return False


def eliminar_pelicula(codigo, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        for c in list(cartelera.keys()):
            if c.lower() == codigo.lower():
                del cartelera[c]
                del peliculas[c]
                return True
    return False


def validar_codigo(codigo, peliculas, cartelera):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo, cartelera):
        return False
    return True


def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True


def validar_duracion(duracion):
    try:
        valor = int(duracion)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False


def validar_clasificacion(clasificacion):
    if clasificacion in ("A", "B", "C"):
        return True
    return False


def validar_es_3d(valor):
    if valor == "s" or valor == "n":
        return True
    return False


def validar_precio(precio):
    try:
        valor = int(precio)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False


def validar_cupos(cupos):
    try:
        valor = int(cupos)
        if valor >= 0:
            return True
        return False
    except ValueError:
        return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False
    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True


def main():
    peliculas = {
        'P101': ['Luz de Otono', 'drama', 110, 'B', 'Espanol', False],
        'P102': ['Noche Neon', 'accion', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Espanol', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Espanol', True],
        'P105': ['Codigo Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficcion', 132, 'B', 'Ingles', False],
    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }

    opcion = 0
    while opcion != 6:
        print("========== MENU PRINCIPAL ==========")
        print("1. Cupos por genero")
        print("2. Busqueda de peliculas por rango de precio")
        print("3. Actualizar precio de pelicula")
        print("4. Agregar pelicula")
        print("5. Eliminar pelicula")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese genero a consultar: ")
            cupos_genero(genero, peliculas, cartelera)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas, cartelera)

        elif opcion == 3:
            respuesta = "s"
            while respuesta == "s":
                codigo = input("Ingrese codigo de pelicula: ")
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                resultado = actualizar_precio(codigo, nuevo_precio, cartelera)
                if resultado:
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:
            codigo = input("Ingrese codigo de pelicula: ")
            titulo = input("Ingrese titulo: ")
            genero = input("Ingrese genero: ")
            duracion = input("Ingrese duracion (minutos): ")
            clasificacion = input("Ingrese clasificacion (A/B/C): ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")

            if not validar_codigo(codigo, peliculas, cartelera):
                print("El codigo no es valido o ya existe")
            elif not validar_texto(titulo):
                print("El titulo no es valido")
            elif not validar_texto(genero):
                print("El genero no es valido")
            elif not validar_duracion(duracion):
                print("La duracion no es valida")
            elif not validar_clasificacion(clasificacion):
                print("La clasificacion no es valida")
            elif not validar_texto(idioma):
                print("El idioma no es valido")
            elif not validar_es_3d(es_3d):
                print("El valor de 3D no es valido")
            elif not validar_precio(precio):
                print("El precio no es valido")
            elif not validar_cupos(cupos):
                print("Los cupos no son validos")
            else:
                es_3d_bool = True if es_3d == "s" else False
                resultado = agregar_pelicula(codigo, titulo, genero, int(duracion), clasificacion, idioma, es_3d_bool, int(precio), int(cupos), peliculas, cartelera)
                if resultado:
                    print("Pelicula agregada")
                else:
                    print("El codigo ya existe")

        elif opcion == 5:
            codigo = input("Ingrese codigo de pelicula: ")
            resultado = eliminar_pelicula(codigo, peliculas, cartelera)
            if resultado:
                print("Pelicula eliminada")
            else:
                print("El codigo no existe")

        elif opcion == 6:
            print("Programa finalizado")


if __name__ == "__main__":
    main()