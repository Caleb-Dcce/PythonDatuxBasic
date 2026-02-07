# Realiza un menu iterativo
# Cada opcion debe ser una funcion => fz()
# Opcion 1 : Sumar 2 numeros
# Opcion 2 : Crea una coleccion de productos para un mercado
# Opcion 3 : Agrega un nuevo producto a la coleccion
# Opcion 4 : Mostrar el producto de precio mas bajo
# Opcion 5 : Salir

menu = """
    De las siguiente opciones
    Opcion 1 : Sumar 2 numeros
    Opcion 2 : Crea una coleccion de productos para un mercado
    Opcion 3 : Agrega un nuevo producto a la coleccion
    Opcion 4 : Mostrar el producto de precio mas bajo
    Opcion 5 : Salir
"""

def sum2num ():
    print("Primero se deben ingresar los números a sumar")
    a=int(input("Ingrese el primer número:"))
    b=int(input("Ingrese el segundo número:"))
    s=a+b
    print(f"El resultado de la suma es {s}")
    iterar()
    return False

productos = [
    {
        'id': 1,
        'nombre': 'Arroz Costeño',
        'categoria': 'Abarrotes',
        'cantidad': 50,
        'UM': 'kg',
        'precio': 3.80,
    },
    {
        'id': 2,
        'nombre': 'Azúcar Rubia',
        'categoria': 'Abarrotes',
        'cantidad': 40,
        'UM': 'kg',
        'precio': 3.20,
    },
    {
        'id': 3,
        'nombre': 'Aceite Vegetal',
        'categoria': 'Abarrotes',
        'cantidad': 25,
        'UM': 'unidades',
        'precio': 9.50,
    },
    {
        'id': 4,
        'nombre': 'Leche Gloria',
        'categoria': 'Lácteos',
        'cantidad': 60,
        'UM': 'unidades',
        'precio': 4.20,
    },
    {
        'id': 5,
        'nombre': 'Pollo Entero',
        'categoria': 'Carnes',
        'cantidad': 30,
        'UM': 'kg',
        'precio': 8.90,
    },
    {
        'id': 6,
        'nombre': 'Manzana Roja',
        'categoria': 'Frutas',
        'cantidad': 20,
        'UM': 'kg',
        'precio': 4.50,
    },
    {
        'id': 7,
        'nombre': 'Papa Blanca',
        'categoria': 'Verduras',
        'cantidad': 100,
        'UM': 'kg',
        'precio': 1.80,
    },
    {
        'id': 8,
        'nombre': 'Pan Francés',
        'categoria': 'Panadería',
        'cantidad': 200,
        'UM': 'unidades',
        'precio': 0.30,
    },
    {
        'id': 9,
        'nombre': 'Huevos',
        'categoria': 'Abarrotes',
        'cantidad': 15,
        'UM': 'maples',
        'precio': 18.00,
    }
]

def lista_productos():
    for p in productos:
        print(f"ID: {p['id']} | "
            f"Nombre: {p['nombre']} | "
            f"Categoría: {p['categoria']} | "
            f"Cantidad: {p['cantidad']} {p['UM']} | "
            f"Precio: S/ {p['precio']}")
    iterar()

def agregar_producto():
    print('Tener en cuenta el siguiente ejemplo:')
    print(
        f"ID: {productos[0]['id']} | "
        f"Nombre: {productos[0]['nombre']} | "
        f"Categoría: {productos[0]['categoria']} | "
        f"Cantidad: {productos[0]['cantidad']} {productos[0]['UM']} | "
        f"Precio: S/ {productos[0]['precio']}")
    nuevo_producto={
        'id':max(p['id'] for p in productos) + 1 if productos else 1,
        'nombre':input('Ingrese el nombre del producto:'),
        'categoria':input('Ingrese el categoria del producto:'),
        'cantidad':input('Ingrese la cantidad del producto:'),
        'UM':input('Ingrese la UM del producto:'),
        'precio':input('Ingrese el precio del producto:')}
    productos.append(nuevo_producto)
    print('Producto agregado correctamente')
    iterar()

def obtener_precio(p):
    return p['precio']

def producto_barato():
    producto = min(productos, key=obtener_precio)
    print('El producto de precio más bajo es:')
    print(
        f"ID: {producto['id']} | "
        f"Nombre: {producto['nombre']} | "
        f"Categoría: {producto['categoria']} | "
        f"Cantidad: {producto['cantidad']} {producto['UM']} | "
        f"Precio: S/ {producto['precio']}"
    )
    iterar()

def iterar():
    confirmacion=input("Deseas volver al menu (si/no):")
    if 'SI'.upper() == confirmacion.upper():
        indice()
    else:
        print("Gracias")

def indice():
    print(menu)
    opcion=int(input("Ingrese la opcion a ejecutar:"))
    if opcion==1:
        sum2num()
    elif opcion==2:
        lista_productos()
    elif opcion==3:
        agregar_producto()
    elif opcion==4:
        producto_barato()
    elif opcion==5:
        print('Gracias')
        pass
    else:
        print("Ingrese una opcion válida")

indice()

pip install pytz

pip install pyodbc