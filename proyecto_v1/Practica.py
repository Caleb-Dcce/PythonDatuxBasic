# 1.agregar tu usuario desde el insert en la tabla usuarios del sistema
# 2.implementar en el menu una opcion referente al sistema inmobiliario con el flujo desarrollado en clase
# crear la carpeta servicio para el modulo agregar en caso sea necesario
# (referencias o ejemplos en el main.py )
# 3. enviar un email con email.py 
# (ya se encuentra configurado e implementado en login solo cambiar el subject ,mensaje y llamarlo en tu funcionalidad implementada)

import sqlite3

def agregar_usuario_propio():
    conexion = sqlite3.connect('/workspaces/PythonDatuxBasic/proyecto_v1/bd-si.db')
    cursor = conexion.cursor()
    
    # Agrego el nombre de mi usuario
    query = "INSERT INTO usuarios_sistema (email, password,nombre, apellido, tipo_usuario, estado, fecha_creacion, fecha_actualizacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    datos = ("dacacees@gmail.com", "123456789","David", "Cespedes", "admin", True, '2026-02-07','2026-02-07')
    
    try:
        cursor.execute(query, datos)
        conexion.commit()
        print("Usuario agregado con éxito.")
    except Exception as e:
        print(f"Error o usuario ya existe: {e}")
    finally:
        conexion.close()

agregar_usuario_propio()