numero_rutas = int(input("\nIngrese el número de rutas: "))
rutas = []

for i in range(numero_rutas):
    ruta_dato = input(f"Ingrese la ruta {i + 1}: ").strip().split(' ', 1)
    rutas.append(ruta_dato)

numero_transicones = int(input("\nIngrese el número de transiciones: "))

for i in range(numero_transicones):
    transicion = input(f"Ingrese la transición {i + 1}: ").strip()
    parte_transicion = transicion.split("/")
    encontrado = False

    for ruta, contenido in rutas:
        parte_ruta_definida = ruta.split('/')
        
        if len(parte_ruta_definida) == len(parte_transicion):
            match_valido = True
            valor_parametro = ""
            
            for r, t in zip(parte_ruta_definida, parte_transicion):
                if r.startswith(':'):
                    valor_parametro = t
                elif r != t:
                    match_valido = False
                    break
            
            if match_valido:
                if valor_parametro:
                    nombre_limpio = contenido.split()[0]
                    print(f"{nombre_limpio} {valor_parametro}")
                else:
                    print(contenido)
                encontrado = True
                break

    if not encontrado:
        print("404 Not Found")    