# 1.agregar tu usuario desde el insert en la tabla usuarios del sistema

import sqlite3

sentencia = """
INSERT INTO usuarios_sistema (email, password,nombre, apellido, tipo_usuario, estado, fecha_creacion, fecha_actualizacion)
VALUES ("dacacees@gmail.com", "123456789","David", "Cespedes", "admin", True, '2026-02-07','2026-02-07');
"""

# establecemos la conexión con la base de datos
with sqlite3.connect('/workspaces/PythonDatuxBasic/proyecto_v1/bd-si.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute(sentencia)
    conexion.commit()
    pass