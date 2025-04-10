
INVproductos = {   
    "producto": "Nike Air Max",
    "talla": "40",
    "color": "Negro",
    "stock": 50 
}

def ver_productos():
    print("--------------------------------------------------------------")
    for clave in INVproductos:
        print(clave,":", INVproductos[clave])
    print("--------------------------------------------------------------")

def Editar():
    Clave_Editar = input("Introduce la clave a editar: ").lower()
    nuevo_Dato = input("Introduce el nuevo dato: ")
    
    if Clave_Editar == "producto":
        INVproductos["producto"] = nuevo_Dato
        
    elif Clave_Editar == "talla":
        INVproductos["talla"] = nuevo_Dato
        
    elif Clave_Editar == "color":
        INVproductos["color"] = nuevo_Dato
        
    elif Clave_Editar == "stock":
        INVproductos["stock"] = nuevo_Dato
    else:
        print("La clave no existe.")
        print("--------------------------------------------------------------")

    
    
    
def Eliminar ():
        
    Clave_Eliminar = input("Introduce la clave a eliminar: ").lower()
    
    if Clave_Eliminar == "producto":
        valor_eliminado = INVproductos.pop("producto")
        print(f"Se ha eliminado el producto: {valor_eliminado}")        
        
    elif Clave_Eliminar == "talla":
        valor_eliminado = INVproductos.pop("talla")
        print(f"Se ha eliminado la talla: {valor_eliminado}") 
        
    elif Clave_Eliminar == "color":
        valor_eliminado = INVproductos.pop("color")
        print(f"Se ha eliminado el color: {valor_eliminado}") 
        
    elif Clave_Eliminar == "stock":
        valor_eliminado = INVproductos.pop("stock")
        print(f"Se ha eliminado el stock: {valor_eliminado}") 
        
    else:
        print("La clave no existe.")
    print("--------------------------------------------------------------")

    
while True:
    ver_productos()
    print("")
    print("--------------------------------------------------------------")
    print("Bienvenido al sistema de gestión de inventario!, ¿qué deseas hacer?")
    print("Editar(1)")
    print("Eliminar(2)")
    print("Salir(3)")
    print("--------------------------------------------------------------")
    
    opcion = input("Elige una opción: ").lower()
    
    if opcion == "1" or opcion == "editar":
        Editar()
    
    elif opcion == "2" or opcion == "eliminar":
        Eliminar()
    
    else:
        print("Programa finalizado.")
        break

ver_productos()
    
    