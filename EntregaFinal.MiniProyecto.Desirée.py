#Imprimimos título del programa.
print("¡Bienvenid@ a nuestra Mini Tienda Online!\n")

#Definición variables:
lista_articulos = [] #Lista con los artículos. Cada artículo: {"id", "nombre", "precio", "stock", "activo"}
lista_usuarios = [] #Lista con los usuarios. Cada usuario:  {"id", "nombre", "email", "activo"}

carrito_actual = [] #Lista de tuplas (articulo_id, cantidad)
usuario_activo = None #ID del usuario que compra ahora (None = no hay usuario seleccionado)
ventas = [] #Lista de las ventas. Cada venta: { "id_venta": int, "usuario_id": int, "items": [(articulo_id, cantidad, precio_unitario)], "total": float }


#Menús
menu_principal = [  #Menú principal con 4 opciones
    "1. Gestión de artículos",
    "2. Gestión de usuarios",
    "3. Ventas / Carrito",
    "4. Salir\n"
]

menu_articulos_opciones = [ #Menú artículos con 7 opciones
    "1. Crear artículos",
    "2. Listar artículos",
    "3. Buscar artículos por ID",
    "4. Actualizar artículos",
    "5. Eliminar artículo",
    "6. Alternar activo/inactivo",
    "7. Salir\n",
]

submenu_articulos = [ #Submenú artículos con 3 opciones
    "1. Ver todos los artículos",
    "2. Ver artículos activos",
    "3. Ver artículos inactivos\n"
]

menu_usuarios_opciones = [ #Menú usuarios con 7 opciones
    "1. Crear usuario",
    "2. Listar usuario",
    "3. Buscar usuario por ID",
    "4. Actualizar usuario",
    "5. Eliminar usuario",
    "6. Alternar activo/inactivo",
    "7. Salir\n"
]

submenu_usuarios = [ #Submenú usuarios con 3 opciones
    "1. Ver todos los usuarios",
    "2. Ver los usuarios activos",
    "3. Ver los usuarios inactivos\n"
]

menu_ventas = [ #Menú ventas con 8 opciones
    "1. Seleccionar usuario activo",
    "2. Añadir artículo al carrito",
    "3. Quitar artículo del carrito",
    "4. Ver carrito (detalle y total)",
    "5. Confirma compra (resta stock y registra venta)",
    "6. Historial de ventas por usuario",
    "7. Vaciar carrito",
    "8. Volver\n",
]

#Definición funciones: COMUNES

#Función Menú. Muestra un menú y devuelve la opción introducia por teclado
def ver_menu(opciones): #Función
    for linea in opciones: #Recorremos cada línea del menú recibido
        print(linea) #Imprime cada línea

    opcion = input("Indique la opción que deseas realizar: ") #Solicitamos al usuario una opción del menú
    return opcion #Devolvemos la opción

#Función Lista vacía. Comprueba si alguna de las listas está vacía
def lista_vacia(lista, mensaje_vacia): #Función 
    if len(lista) == 0: #Si la lista no tiene elementos
        print(mensaje_vacia) #Mostramos mensaje de lista vacía
        return False #Indica a la función que no hay elementos
    return True #Si sí hay elimentos, devolvemos True para continuar

#Función - Generar ID único para una lista 
def generar_id(lista_items, clave_id): #Función
    if not lista_items: #Si la lista está vacía el primer ID que creará será el 1
        return 1
    
    maximo_id = lista_items[0][clave_id] #Empezamos suponiendo que el 1º elemento tiene el id máximo
    for elemento in lista_items: #Recorremos todos los elementos dentro de la lista
        if elemento[clave_id] > maximo_id: #Si encuentra un id mayor
            maximo_id = elemento[clave_id] #Si es mayor, se guarda como nuevo máximo
    
    return maximo_id + 1 #El nuevo ID será el máximo + 1, para garantizar que no se repita
        
#Definición funciones: ARTÍCULOS.
#Función - Crear artículos
def crear_articulos(articulos): #Función 
    nombre_valido = False #Variable booleana. Nos sirve como condición de salida del bucle while.
    while nombre_valido == False: #Mientras el valor inválido, el bucle pedirá el dato y lo validará.
        nombre = str(input("Indique el nombre del artículo que deseas añadir: "))
        if len(nombre) > 0: #Si tiene al menos 1 carácter, es válido.
            nombre_valido = True
        else:
            print("El nombre del artículo no puede estar vacío.\n")
    
    precio_valido = False #Variable booleana. Nos sirve como condición de salida del bucle while.
    while precio_valido == False: #Mientras el valor inválido, el bucle pedirá el dato y lo validará.
        precio = float(input(f"Introduzca el precio de {nombre}, (debe ser mayor a 0€): "))
        if precio > 0: #Si el usuario introduce un precio valido pasa a True y el bucle terminará.
            precio_valido = True
        else:
            print("El valor introducido debe ser mayor a 0.\n")
            
    stock_valido = False
    while stock_valido == False: 
        stock = int(input(f"Indique cuantes unidades incluimos en {nombre}, (debe ser superior >= 0): "))
        if stock > 0:
            stock_valido = True
        else:
            print("El valor introducido debe ser mayor a 0.\n")
    
    diccionario_articulos = {
        "id": generar_id(articulos, "id"), #Llama a la función
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True, #Nos servirá para  mostrar si el artículo está activo o inactivo: True o False.
    }
    articulos.append(diccionario_articulos) #Inclumos el nuevo artículo creado al final de la lista principal.
    print(f"{nombre} se ha incluido en el inventario con ID {diccionario_articulos['id']}.\n") #Mostramos resultado al usuario.

#Función - Listar artículos. Para mostrar en pantalla todos los artículos que tenemos en la lista.
def listar_articulos(articulos): #Función
    if not lista_vacia(articulos, "No hay artículos disponibles.\n"): #Llamamos a la función lista_vacía
        return #Salir si no hay artículos. No nos devuelve nada.
    
    opcion = ver_menu(submenu_articulos) #Mostramos el submenú al usuario
    
    match opcion: #Usamos match para que pueda seleccionar una de las opciones
        case "1": #Ver todos los artículos. 
            for a in articulos: #Recorre la lista de artículos y se muestra al usuario. 
                print(f"ID: {a['id']}, Nombre: {a['nombre']}, Precio: {a['precio']}€, Stock: {a['stock']} unidades, Activo: {a['activo']}.\n")
        case "2": #Ver los artículos activos.
            encontrados_activos = 0 #Contador para saber si hay artículos activos.
            for a in articulos:
                if a['activo'] == True:
                    print(f"ID: {a['id']}, Nombre: {a['nombre']}, Precio: {a['precio']}€, Stock: {a['stock']} unidades, Activo: {a['activo']}.\n")
                    encontrados_activos += 1 #Suma 1 cada vez que se encuentra un activo.
            if encontrados_activos == 0: #Si no se han encontrado artículos activos se muestra al usuario.
                print("No hay artículos activos en este momento.\n")
        case "3": #Ver los artículos inactivos.
            encontrados_inactivos = 0 #Contador para saber si hay artículos inactivos.
            for a in articulos:
                if a['activo'] == False:
                    print(f"ID: {a['id']}, Nombre: {a['nombre']}, Precio: {a['precio']}€, Stock: {a['stock']} unidades, Activo: {a['activo']}.\n")
                    encontrados_inactivos += 1 #Suma 1 cada vez que se encuentra un inactivo.
            if encontrados_inactivos == 0: #Si no se han encontrado artículos inactivos se muestra al usuario.  
                print("No hay artículos inactivos en estos momentos.\n")  
        case _: #Si ninguna de las opciones seleccionadas del submenú es correcta.      
            print("No has seleccionado una opción correcta.\n")
            
    return #Salir

#Función - Buscar artículo por ID
def buscar_articulo_id(articulos): #Función. 
    if not lista_vacia(articulos, "No disponemos de artículos.\n"): #
        return None #Devuelve un valor (el artículo encontrado o nada)
    
    busqueda_id = int(input("Indique el ID del artículo: ")) #Solicitamos al usuario que introduzca el ID que quiere buscar.

    for a in articulos: #Recorremos la lista de artículos uno a uno. En cada vuelta, a será un diccionario.
        if a["id"] == busqueda_id: #Accede al valor de la clave "id" dentro del diccionario a. Si coincide con el que ha introducido el usuario es el artículo que buscabamos. 
            print(f"El artículo cuyo ID es {busqueda_id} ha sido encontrado.\nID: {a['id']}, Nombre: {a['nombre']}, Precio: {a['precio']}€, Stock: {a['stock']} unidades, Activo: {a['activo']}.\n")
            return a #Devuelve el diccionario completo del artículo encontrado. Así otras funciones pueden usar ese mismo artículo. 
            
    #Si no ha encontrado nada, se muestra:
    print(f"El artículo con ID {busqueda_id} no ha sido encontrado.\n")
    return None #Indica que no se encontró nada y la función finaliza. 

#Función - Obtener artículo por ID
def obtener_articulo_por_id(articulos, id_buscar): #Devuelve el diccionario o None. No interactivo.
    for a in articulos:
        if a["id"] == id_buscar:
            return a
        return None
    
#Función - Actualizar artículos (nombre, precio y stock)
def actualizar_articulos(articulos): #Función.
    if len(articulos) == 0: #Devuelve cuántos elementos hay en la lista, si es igual a 0, está vacía.
        print("No disponemos de artículos.\n")
        return #Salir función.
    
    #Llamamos a otra función (buscar_articulos_id) para pedir al usuario un ID y busca el artículo dentro de la lista. 
    #Si encuentra el artículo devuelve el diccionario del artículo. Sino, devuelve None. 
    articulo_modificar = buscar_articulo_id(articulos)
    if articulo_modificar is None:
        return #Si la función anterior devolvió None, no encontró el artículo, Return nos hace salir de la función para no continuar lo siguiente. 
    
        #Solicitamos un nuevo nombre para el artículo
    nuevo_nombre = input("Indique el nombre que quieres poner al artículo: ")
    articulo_modificar["nombre"] = nuevo_nombre #Accede al valor de 'nombre' dentro del diccionario y le asigna el nombre que ha introducido el usuario. 
    
    #Solicitamos un nuevo precio para el artículo
    nuevo_precio = float(input("Introduce un nuevo precio para el artículo, (debe ser mayor a 0€): "))
    if nuevo_precio > 0:
        articulo_modificar["precio"] = nuevo_precio #Si es mayor a 0, se actualiza el precio.
        
    else: #Sino, muestra mensaje de error.
        print("El precio introducido no es válido. Debe ser mayor a 0.\n")
        
    #Solicitamos un nuevo número de unidades de stock
    nuevo_stock = int(input("Introduce el número de unidades de stock, (debe ser mayor a 0): "))
    if nuevo_stock > 0:
        articulo_modificar["stock"] = nuevo_stock
        
    print("El artículo ha sido actualizado en la lista.\n")

#Función - Eliminar artículos    
def eliminar_articulos(articulos): #Función
    if not lista_vacia(articulos, "No disponemos de artículos.\n"): #Llamamos a la función lista_Vacia
        return #Salir función

    #Llamamos a la función de buscar artículo ID
    articulo_eliminar = buscar_articulo_id(articulos)
    if articulo_eliminar != None: #Si el artículo encontrado es distinto a None, es decir, si existe, lo eliminamos. 
        articulos.remove(articulo_eliminar)
        print("El artículo ha sido eliminado.\n")

#Función - Alternar estado Activo/Inactivo 
def alternar_estado(articulos): #Función
    if not lista_vacia(articulos, "No disponemos de artículos.\n"): #Llamamos a la función lista_Vacia
        return #Salir funciómn
    
    articulo = buscar_articulo_id(articulos) #Se llama a la función de búsqueda de ID y será ella quién solicite el ID
    
    #Guardamos el artículo anterior y cambiamos su valor.
    if articulo != None: #Si el artículo encontrado es distinto a None, existe, entonces, lo modificamos. 
        articulo["activo"] = not articulo["activo"] #Cambiamos el estado de True o False con not. Si está activo para a inactivo y lo mismo al revés.
        print("El estado del producto ha cambiado.\n")
        
#Definición funciones: USUARIOS

#Función simple para valicación del email (contenga "@" y ".")
def validar_email(email):
    if "@" in email and "." in email: #Comprueba si ambos caracteres aparecen en el texto. 
        return True #Si ambas condiciones se cumplen nos devuelve True, el email es válido.
    else:
        return False #Sino, nos devuelve False.

#Función crear usuarios
def crear_usuarios(usuarios): 
    nombre_valido = False #Bandera booleana para repetir la petición hasta que el nombre sea válido.
    while nombre_valido == False:
        crear_usuario = input("Indique el nombre del usuario que quieres crear: ") #Solicitamos un nombre.
        if len(crear_usuario) > 0: #Obliga a que el nombre no esté vacío. Si no lo está, da el nombre por válido.
            nombre_valido = True
        else: #Sino, indica al usuario que el nombre no puede estar vacío.
            print("El nombre no puede estar vacío.\n")
    
    #Solicitamos un email
    email_valido = False
    while email_valido == False:
        crear_email = input(f"Indique el email de {crear_usuario}: ")
        if validar_email(crear_email):
            email_valido = True
        else:
            print("El email introducido no es válido. Debe contener '@' y '.'\n")
            
    #Creamos un diccionario con los datos del usuario:
    diccionario_usuarios = { 
        "id": generar_id(usuarios, "id"), #Llamada a generar_id
        "nombre": crear_usuario, 
        "email": crear_email,
        "activo": True
    }
    
    #Añade el diccionario a la lista principal.
    usuarios.append(diccionario_usuarios)
    #Imprimos confirmación.
    print(f"Usuario: {crear_usuario}, creado con el ID {diccionario_usuarios['id']}.\n")
    
#Función listar usuarios
def listar_usuarios(usuarios): #Función
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"): #Llamamos a la función lista_vacia
        return #Si está vacía, salimos
    
    #Imprimimos submenú usuarios
    opcion = ver_menu(submenu_usuarios)
    match opcion:
        case "1":
            for u in usuarios:
                print(f"ID: {u['id']}, Nombre: {u['nombre']}, Email: {u['email']}, Activo: {u['activo']}.\n")
        case "2":
            encontrados_activos = 0
            for u in usuarios:
                if u['activo'] == True:
                    print(f"ID: {u['id']}, Nombre: {u['nombre']}, Email: {u['email']}, Activo: {u['activo']}.\n")
                    encontrados_activos += 1 #Suma 1 cada vez que se encuentra un activo.
            if encontrados_activos == 0: #Si no se han encontrado usuarios activos se muestra al usuario.
                print("No hay usuarios activos en este momento.\n")
        case "3":
            encontrados_inactivos = 0
            for u in usuarios:
                if u['activo'] == False:
                    print(f"ID: {u['id']}, Nombre: {u['nombre']}, Email: {u['email']}, Activo: {u['activo']}.\n")
                    encontrados_inactivos += 1 #Suma 1 cada vez que se encuentra un activo.
            if encontrados_inactivos == 0: #Si no se han encontrado inactivos se muestra al usuario.
                print("No hay usuarios inactivos en este momento.\n")
            
        case _:
            print("La opción introducida no es válida.\n")
            
    return #Salir
    
#Función buscar usuario por ID
def buscar_usuario_id(usuarios):
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"): #Llamamos a la función lista_vacia
        return None
    
    #Solicitamos que nos indique el ID del usuario.
    busqueda_id = int(input("Indique el ID del usuario: "))
    
    for u in usuarios: #Recorremos la lista de usuarios uno a uno.
        if u["id"] == busqueda_id: #Recorre la lista y compara u["id"] con el busqueda_id.
            print(f"El usuario cuyo ID es {busqueda_id} ha sido encontrado.\nID: {u['id']}, Nombre: {u['nombre']}, Email: {u['email']}, Activo: {u['activo']}.\n")
            return u #Envía el diccionario de vuelta a la función que llamó a buscar_usuario_id. Así, desde otras funciones se puede usar esta función.
    
    #Si no ha encontrado nada, se imprime al usuario.
    print(f"El usuario con ID {busqueda_id} no ha sido encontrado.\n")
    return None #Si el bucle termina sin coincidencias, muestra el mensaje anterior y devuelve None.

#Función - Obtener usuario por ID
def obtener_usuario_por_id(usuarios, id_buscar): #Devuelve el diccionario o None
    for u in usuarios:
        if u["id"] == id_buscar:
            return u
        return None

#Función actualizar usuario
def actualizar_usuario(usuarios):
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"): #Si no hay usuarios, salimos
        return
    
    usuario_modificar = buscar_usuario_id(usuarios) #Llamamos a la función de búsqueda de ID
    if usuario_modificar is None: #Pedimos ID, si no existe, salimos de la función
        return
    
    #Solicitamos un nuevo nombre para el usuario
    nuevo_nombre = input("Indique el nuevo nombre que quieres poner al usuario: ")
    if len(nuevo_nombre) > 0: #Si validamos, actualizamos
        usuario_modificar["nombre"] = nuevo_nombre #Actualiza el campo 'nombre' en el diccionario del usuario. 
    
    #Solicitamos nuevo email
    nuevo_email = input(f"Indique el nuevo email para {nuevo_nombre}: ")
    if validar_email(nuevo_email): #Llama a la función validar_email directamente. Si devuelve True lo guarda en el diccionario y sino, muestra error.
        usuario_modificar["email"] = nuevo_email 
        print("El email se ha modificado correctamente.\n")
    else:
        print("El email introducido no es válido. Debe contener '@' y '.'\n")
    
#Función eliminar usuario
def eliminar_usuario(usuarios):
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"):
        return #Si la lista está vacía, salimos
    
    usuario_eliminar = buscar_usuario_id(usuarios) #Llamamos a la función de búsqueda de ID
    if usuario_eliminar != None: #Si el usuario encontrado es distinto a None, es decir, existe, lo eliminamos.
        usuarios.remove(usuario_eliminar)
    return #Salir
    
#Función alternar activo/inactivo
def alternar_usuarios(usuarios):
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"):
        return 
    
    usuario_alternar = buscar_usuario_id(usuarios)
    if usuario_alternar !=  None: #Busca usuario por ID, si existe, invirte el valor booleano. 
        usuario_alternar["activo"] = not usuario_alternar["activo"]
        print("El estado del usuario ha cambiado.\n")
        
#Definición funciones: VENTAS / CARRITO

def seleccionar_usuario_activo(usuarios): #Selecciona el usuario que hará la compra (debe existir y estar activo)
    global usuario_activo #Modificamos la global
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"):
        return
    
    usuario = buscar_usuario_id(usuarios) #Llamamos a la función
    if usuario is None:
        return
    if usuario["activo"] == False: #Si el usuario está inactivo
        print("Este usuario está inactivo. Debes activarlo primero.\n")
        return    
    
    usuario_activo = usuario["id"]
    print(f"Usuario activo seleccionado: {usuario['nombre']} (ID {usuario_activo})\n")
    
def añadir_articulos_carritos(articulos):
    global carrito_actual #Modificamos la lista global del carrito
    
    if not lista_vacia(articulos, "No hay artículos para vender.\n"):
        return #Si no hay artículos, salimos
    
    articulo = buscar_articulo_id(articulos)
    if articulo is None:
        return #Buscamos por ID, si no existe, salimos
    
    if articulo["activo"] == False: #Si está inactivo, mostramos mensaje
        print("El artículo está inactivo. No se puede añadir al carrito.\n")
        return
    
    if articulo["stock"] <= 0: #Si no hay stock
        print("No disponemos de stock de ese artículo.\n")
        return
    
    cantidad_valida = False #Booleano para validar cantidad
    while cantidad_valida == False: #Pedimos cantidad hasta que sea válida
        cantidad = int(input(f"¿Cuántas unidades de '{articulo['nombre']}' quieres añadir al carrito? Debes tener en cuenta el máximo {articulo['stock']}): "))
        if 0 < cantidad <= articulo["stock"]:
            cantidad_valida = True #Acepto
        else:
            print("La cantidad introducida no es válida.\n")
            
    existe_carrito = False #Si ya existía el artículo en el carrito
    for i, (articulo_id, cant) in enumerate(carrito_actual): #Recorre carrito
        if articulo_id == articulo["id"]: #Si el artículo ya está
            carrito_actual[i] = (articulo_id, cant + cantidad) #Sumamos cantidades
            existe_carrito = True #Marcamos si ya estaba
    if existe_carrito == False: #Si no estaba en el carrito   
        carrito_actual.append((articulo['id'], cantidad)) #Agregamos el artículo y cantidad como tupla
        
    #Mostramos confirmación
    print(f"Se añadieron {cantidad} ud(s). de '{articulo['nombre']}' al carrito de compra.\n")
        
def quitar_articulo_carrito():
    global carrito_actual #Elimina un artículo del carrito por ID si se encuentra
    
    if not lista_vacia(carrito_actual, "El carrito está vacío"): #Si el carrito está vacío, salimos
        return
    
    articulo = buscar_articulo_id(lista_articulos) #Llamamos a la función de búsqueda de artículos. Pedirá el ID y devolverá el diccionario del artículo.
    if articulo is None: #Si no se encontró, salimos
        return
    
    id_objetivo = articulo["id"]
    
    nuevo_carrito = [] #Creamos un nuevo carrito sin ese artículo
    eliminar = False
    
    for art_id, cant in carrito_actual: #Recorremos las tuplas del carrito (id, cantidad)
        if art_id == id_objetivo: #Si coincide, lo marcamos para eliminar
            eliminar = True
        else:
            nuevo_carrito.append((art_id, cant)) #Si no, lo conservamos
            
    carrito_actual = nuevo_carrito #Reemplazamos el carrito anterior por el nuevo
    
    #Mensaje al usuario según resultado
    if eliminar:
        print(f"Se ha eliminado '{articulo['nombre']} del carrito.\n")
    else:
        print(f"'{articulo['nombre']} no se encuentra en el carrito.\n") 
        
def ver_carrito(articulos):
    if not lista_vacia(carrito_actual, "El carrito está vacio.\n"):
        return
    
    total = 0
    for articulo_id, cant in carrito_actual: #Recorro tuplas (id, cantidad)
        articulo = obtener_articulo_por_id(articulos, articulo_id) #Buscamos el artículo en la lista
        if articulo is None: #Si el artículo fue borrado, continuamos
            continue
        subtotal = articulo["precio"] * cant #Precio unitario por cantidad
        total += subtotal #Acumulamos el total
        print(f" - {articulo['nombre']} (ID {articulo['id']}): {cant} ud(s) x {articulo['precio']}€, subtotal = {subtotal}.\n") #Mostramos línea completa
    print(f"Total: {total}€.\n") #Mostramos el total

def confirmar_compra(articulos, usuarios, ventas): #Función
    global carrito_actual, usuario_activo #Modificaré estos globales
    
    if usuario_activo is None: #Debe haber usuario activo, sino, salimos
        print("Antes de comprar selecciona un usuario activo.\n")
        return
    
    usuario = obtener_usuario_por_id(usuarios, usuario_activo) #Verificamos que existe
    if usuario is None or usuario["activo"] == False: #Verificamos que esté activo
        print("El usuario no existe o se encuentra inactivo.\n")
        return
    
    if not lista_vacia(carrito_actual, "El carrito está vacío.\n"): #El carrito debe tener artículos
        return
    
    #Verificación previa
    for articulo_id, cant in carrito_actual: #Recorremos cada línea del carrito
        articulo = buscar_articulo_id(articulos, articulo_id) #Buscamos el artículo
        if articulo is None or articulo["activo"] == False: #Si no existe o está inactivo
            print("Los artículos no están disponibles, no existen o se encuentran inactivos.\n")
            return
        if cant > articulo["stock"]: #Si la cantidad es mayor al stock
            print("No hay stock suficiente para ese artículo.\n")
            return
        
    #Si en la verificación está todo bien
    items_venta = [] #guardo las tuplas (id, cant, precio_unitario)
    total = 0 #Contador venta
    for articulo_id, cant in carrito_actual:
        articulo = buscar_articulo_id(articulos, articulo_id) #Recorremos carrito y obtenemos el artículo
        precio_unidad = articulo["precio"] #Precio actual
        subtotal = precio_unidad * cant #Calculo subtotal
        total += subtotal #Suma total
        articulo["stock"] = articulo["stock"] - cant #Resto del stock
        items_venta.append((articulo_id, cant, precio_unidad)) #Guardamos venta
        
    #Registro de la venta
    venta = {
        "id_venta": generar_id(ventas, "id_venta"), #ID único de venta
        "usuario_id": usuario_activo, #ID del usuario que compró
        "items": items_venta, #Lista de tuplas (articulo_id, cantidad, precio_unitario)
        "total": total #Total final
    }
    ventas.append(venta) #Añado la venta al listado de ventas
    carrito_actual = [] #Vaciamos el carrito
    #Resultado
    print(f"{usuario['nombre']}, se ha confirmado la compra.\n Importe total: {total}€\n")

#Función auxiliar para buscar nombre de artículo
def obtener_nombre_articulo(articulo, articulo_id):   
    if articulo is not None:
        return articulo["nombre"]
    else:
        return f"Artículo {articulo_id}"   
    
def historial_ventas_usuario(usuarios, ventas, articulos): #Función
    if not lista_vacia(usuarios, "No hay usuarios registrados.\n"):
        return

    if not lista_vacia(ventas, "No hay ventas registradas.\n"):
        return
    
    usuario = obtener_usuario_por_id(usuarios) #Buscamos usuario por ID, si no existe, salimos
    if usuario is None:
        return
    
    existen_ventas = False #Booleano para saber si hay ventas
    for v in ventas: #Recorremos la lista de ventas
        if v["usuario_id"] == usuario["id"]: #Si son del usuario
            existen_ventas = True #Sí hay
            print(f"ID venta: {v['id_venta']}, total: {v["total"]}€.\n")
            for (articulo_id, cant, precio_unidad) in v["items"]: #Recorremos las líneas de venta
                articulo = obtener_articulo_por_id(articulos, articulo_id) #Intentamos obtener el artículo
                
                nombre = obtener_nombre_articulo(articulo, articulo_id) #Llamamos a la función buscar nombre artículo
                print(f" - {nombre}: {cant} ud(s) x {precio_unidad}€.\n")
    if existen_ventas == False: #Si no hubo ventas
        print("El usuario no tiene ventas registradas en nuestra base de datos.\n")

def vaciar_carrito(): #Función vaciar el carrito
    global carrito_actual #Modificamos el carrito actual global
    carrito_actual = [] #Asignamos una nueva lista vacía
    print("El carrito se ha vaciado.\n")
    
#Lógica programación:
#Mostramos menú principaly solicitamos que indique la opción que desea realizar.
opcion_principal = ver_menu(menu_principal) #Mostramos menú principal y leemos la opción

#Bucle while hasta que el usuario finalice la lista
while opcion_principal != '4': #Mientras no elija la opción 4
    match opcion_principal:
        case "1": #Opción 1 del menú principal. Nos lleva al menú de artículos.
            opcion_articulos = ver_menu(menu_articulos_opciones) #Mostramos el menú de artículos.
            while opcion_articulos != '7': #Mientras no elija la opción 7
                match opcion_articulos:
                    case "1":
                        crear_articulos(lista_articulos)
                    case "2":
                        listar_articulos(lista_articulos)
                    case "3":
                        buscar_articulo_id(lista_articulos)
                    case "4":
                        actualizar_articulos(lista_articulos)
                    case "5":
                        eliminar_articulos(lista_articulos)
                    case "6":
                        alternar_estado(lista_articulos)
                    case _:
                        print("La opción del menú que has introducido no es válida. Por favor, inténtelo de nuevo.\n")

                #Mostramos de nuevo el menú de artículos.
                opcion_articulos = ver_menu(menu_articulos_opciones) #Volvemos a mostrar menú artículos dentro del bucle
                
        case "2": #Opción 2 del menú principal. Nos lleva al menú de usuarios.
            opcion_usuarios = ver_menu(menu_usuarios_opciones) #Mostramos el menú de usuarios.
            while opcion_usuarios != '7':
                match opcion_usuarios:
                    case "1":
                        crear_usuarios(lista_usuarios)
                    case "2":
                        listar_usuarios(lista_usuarios)
                    case "3":
                        buscar_usuario_id(lista_usuarios)
                    case "4":
                        actualizar_usuario(lista_usuarios)
                    case "5":
                        eliminar_usuario(lista_usuarios)
                    case "6":
                        alternar_usuarios(lista_usuarios)
                    case _:
                        print("La opción del menú que has introducido no es válida. Por favor, inténtelo de nuevo.\n")
                
                #Mostramos de nuevo el menú de usuarios.
                opcion_usuarios = ver_menu(menu_usuarios_opciones) #Volvemos a mostrar menú usuarios dentro del bucle
        
        case "3":
            opcion_ventas = ver_menu(menu_ventas) #Mostramos menú ventas    
            while opcion_ventas != '8':
                match opcion_ventas:
                    case "1":
                        seleccionar_usuario_activo(lista_usuarios)
                    case "2":
                        añadir_articulos_carritos(lista_articulos)
                    case "3":
                        quitar_articulo_carrito()
                    case "4":
                        ver_carrito(lista_articulos)
                    case "5":
                        confirmar_compra(lista_articulos, lista_usuarios, ventas)
                    case "6":
                        historial_ventas_usuario(lista_usuarios, ventas, lista_articulos)
                    case "7":
                        vaciar_carrito()
                    case _:
                        print("La opción del menú que has introducido no es válida. Por favor, inténtelo de nuevo.\n")
                
                opcion_ventas = ver_menu(menu_ventas) #Mostramos de nuevo el menú ventas

    #Mostramos de nuevo el menú principal dentro de su bucle
    opcion_principal = ver_menu(menu_principal)  

#Mensaje despedida
print("\nGracias por usar nuestra Mini Tienda Online. ¡Hasta pronto!\n")