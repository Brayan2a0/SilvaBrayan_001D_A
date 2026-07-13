def validar_codigo(codigo:str):
    codigo = codigo.strip()
    
    if codigo != "":
        if codigo and juegos and inventario:
            return False
        
    
    return True

def validar_titulo(titulo:str):
    return titulo.strip() != ""

def validar_plataforma(plataforma:str):
    return plataforma.strip() != ""

def validar_genero(genero:str):
    return genero.strip() != ""

def validar_clasificacion(clasificacion:str):
    clasificacion = clasificacion.upper()
    if clasificacion not in ["E, T, M"]:
        return True
    
    return False

def validar_multiplayer(valor:str):
    if valor == "s" or valor == "n":
        return True
    
    return False

def validar_editor(editor:str):
    return editor.strip() != ""

def validar_precio(precio:int):
    try:
        precio=int(input("Ingrese el precio: "))
        if precio >0:
            return True
        else:
            print("Error: El precio debe ser un entero o maor que cero")
            return False
    except ValueError:
        print("Error: El precio debe ser mayor a 0")
        return False

def validar_stock(stock:int):
    try: 
        stock=int(input("Ingrese el precio: "))
        if stock >=0:
            return True
        else:
            print("Error: El stock tiene que ser un numero positivo")
            return False
    except ValueError:
        print("Error: El stock no ")
        return False

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataformas")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Acualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")

def leer_opcion():
    try:
        opcion=int(input("Ingrese una de las opciones [1/6]: "))
        if opcion == 1:
            return opcion
    except ValueError:
        print("Error: Solo ingrese [1/6]")
        return
    print("Error: Opcion no válida")
    return

def stock_plataforma(plataforma:str, juegos:dict, inventario:dict):
    total=0
    plataforma=plataforma.lower()
    
    if plataforma and juegos:
        if plataforma and inventario:
            for codigo in inventario:
                
                inventario[codigo][1]
        return total
    else:
        return False

def busqueda_precio(p_min:int, p_max:int, juegos:dict, inventario:dict):
    for p_min in inventario:
        pass
    pass

def buscar_codigo(codigo:str, inventario:dict):
    for codigo in inventario:
        codigo=codigo[0]
        return True
    return False

def agregar_juego(codigo:str, titulo:str, plataforma:str, genero:str, claseficacion:str, multiplayer:str, editor:str, precio:int, stock:int, juegos:int, inventario:dict):
    pass

def elininar_juego(codigo:str, juego:dict, inventario:dict):
    pass




juegos =[]

inventario=[]

# juegos = {
# 'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
# 'NovaStudio'],
# 'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
# 'BrightWorks'],
# 'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
# 'OrionGames'],
# 'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
# 'VelocityLab'],
# 'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
# 'GreenSeed'],
# 'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
# 'IronGate']
# }
# inventario = {
# 'G001': [9990, 7],
# 'G002': [19990, 0],
# 'G003': [42990, 3],
# 'G004': [14990, 5],
# 'G005': [17990, 9],
# 'G006': [39990, 2],
# }


while True:
    mostrar_menu()
    opcion=leer_opcion()
    
    if opcion == 1:
        plataforma=input("Ingrese plataforma a consultar: ")
        resultado=stock_plataforma(plataforma,juegos, inventario)
        print(f"El total de stock dispoible: {resultado}")
    elif opcion == 2:
        try:
            p_min=int(input("Ingrese el precio minimo"))
            p_max=int(input("Ingrese el precio maximo"))
            resultado=buscar_codigo(p_min,p_max, juegos, inventario)
        except ValueError:
            print("Error: Solo ingrese número")
    elif opcion == 3:
        codigo=input("Ingrese el codigo del juego").lower()
        nuevo_precio=int(input("Ingrese el nuevo precio"))
        resultado=buscar_codigo(nuevo_precio)
        continuar=input("¿Desea actualizar otro precio (s/n)?: ")
    elif opcion == 4:
        codigo=input("Ingrese código del juego: ")
        resultado=validar_codigo(codigo)
        if resultado == False:
            print("Error: El codigo esta vacio")
            break
        
        titulo=input("Ingrese titulo:")
        resultado=validar_titulo(titulo)
        if resultado == False:
            print("Error: El titulo esta vacio")
            break
        
        plataforma=input("Ingrese la plataforma del juego: ")
        resultado=validar_plataforma(plataforma)
        if resultado == False:
            print("Error: El plataforma esta vacio")
            break
        
        genero=input("Ingrese el género: ")
        resultado=validar_genero(genero)
        if resultado == False:
            print("Error: El género esta vacio")
            break
        
        clasificacion=input("Ingrese el género ['E','T','M']: ")
        resultado=validar_clasificacion(clasificacion)
        if resultado == False:
            print("Error: El género del juego debe ser [E,T,M]: ")
            break
        
        multipleyer=input("Ingrese si es multipleyer [s/n]: ")
        resultado=validar_multiplayer(multipleyer)
        if resultado == False:
            print("Error: El multipleyer tiene que tener una respuesta de s o de n")
            break
        
        editor=input("Ingrese el editor del juego")
        resultado=validar_editor(editor)
        if resultado == False:
            print("Error: El editor esta vacio")
            break
        
        precio=int(input("Ingrese el precio del juego"))
        resultado= validar_precio(precio)
        if resultado == False:
            print("Error: Solo ingrese un número maor que cero")
            break
        
        stock=int(input("Ingrese el stock del juego"))
        resultado=validar_stock(stock)
        if resultado == False:
            print("Error: Debe ser un número mayor o igual a cero")
            break
        
        print("Juego agregado")
        
    elif opcion == 5:
        pass
    elif opcion == 6:
        print("Programa finalizado.")
        exit()
    else:
        print("Error: Opcion no válida")