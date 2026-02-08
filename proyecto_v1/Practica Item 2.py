# 2.implementar en el menu una opcion referente al sistema inmobiliario con el flujo desarrollado en clase
# crear la carpeta servicio para el modulo agregar en caso sea necesario
# (referencias o ejemplos en el main.py )

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box
import pyfiglet
from config.config import ConfigBd
import random
from datetime import datetime
from usuarios.userservices import Login,WelcomeUser
from sqlite3 import Connection
import sqlite3
from config.email import EmailService
console = Console()
config = ConfigBd()
conn = config.bd
emailService = EmailService()

def getMenu(conn:Connection):
    """Menú principal con login y salir"""
    titulo_figlet = pyfiglet.figlet_format("SISTEMA INMOBILIARIO DATUX", font="slant")
    console.print(titulo_figlet, style="bold cyan")
    console.print() # imprime
        
    while True:
        console.clear()
        
        # Panel de bienvenida con pyfiglet

        # Opciones del menú (sin tabla)
        console.print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        console.print("[bold white]  1.[/bold white] [green]Login[/green]")
        console.print("[bold white]  2.[/bold white] [red]Salir[/red]")
        console.print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        console.print()
        
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2"], default="1")
        if opcion == "1":
            # Proceso de login
            console.print("\n[bold yellow]Ingreso al Sistema[/bold yellow]")
            
            usuario = Prompt.ask("Usuario (email)")
            password = Prompt.ask("Contraseña")
            # password=True
            if usuario:
                login=Login(usuario,password,conn)
                if not login:
                    console.print(f"\n[bold red]Login incorrecto! {usuario}[/bold red]")
                    continue
                
                console.print(f"\n[bold green]Login exitoso! Bienvenido {usuario}[/bold green]")
                type_user = login['type_user']
                print(type_user)
                # Determinar qué menú mostrar según el tipo de usuario
                #tipo_usuario = ['admin',"ventas"]
                #random_element = random.choice(tipo_usuario)   
                WelcomeUser(login['user'],emailService)
                if type_user == "admin":
                    getMenuAdmin()
                elif type_user == "ventas":
                    getMenuSale()
                    
            else:
                console.print("\n[bold red]Usuario o contraseña incorrectos[/bold red]")
                console.input("\nPresione Enter para continuar...")
                
        elif opcion == "2":
            if Confirm.ask("\n¿Está seguro que desea salir?"):
                console.print("\n[bold green]¡Hasta luego![/bold green]")
                break

def getMenuAdmin():
    """Menú para administradores"""
    while True:
        console.clear()
        admin_panel = Panel(
            Text("MENÚ ADMINISTRADOR", style="bold green"),
            style="bright_green",
            box=box.DOUBLE
        )
        console.print(admin_panel)
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Descripción", style="white")
        
        table.add_row("1", "Resumen de Pagos")
        table.add_row("0", "Cerrar Sesión")
        
        console.print(table)
        
        opcion = Prompt.ask("Seleccione una opción", choices=["0", "1"])
        
        if opcion == "1":
            resumen_pagos()
        elif opcion == "0":
            console.print("\n[yellow]Cerrando sesión...[/yellow]")
            break
        else:
            console.print(f"\n[bold blue]Función pendiente de implementar: Opción {opcion}[/bold blue]")
            console.input("Presione Enter para continuar...")
            pass

def getMenuSale():
    """Menú para personal de ventas"""
    while True:
        console.clear()
        
        sales_panel = Panel(
            Text("MENÚ VENTAS", style="bold blue"),
            style="bright_blue",
            box=box.DOUBLE
        )
        console.print(sales_panel)
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Descripción", style="white")
        
        table.add_row("1", "Ver Propiedades")
        table.add_row("2", "Registrar Cliente")
        table.add_row("0", "Cerrar Sesión")
        
        console.print(table)
        
        opcion = Prompt.ask("Seleccione una opción", choices=["0", "1", "2"])
        
        if opcion == "1":
            ver_propiedades()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "0":
            console.print("\n[yellow]Cerrando sesión...[/yellow]")
            break
        else:
            console.print(f"\n[bold blue]Función pendiente de implementar: Opción {opcion}[/bold blue]")
            console.input("Presione Enter para continuar...")
            pass

def ver_propiedades():
    conn = sqlite3.connect('/workspaces/PythonDatuxBasic/proyecto_v1/bd-si.db')
    cursor = conn.cursor()
    
    # Seleccionamos las columnas clave que aparecen en tu imagen_889d3a.png
    query = """
    SELECT codigo_producto, titulo, tipo_propiedad, direccion, precio, moneda, estado 
    FROM productos
    """
    
    try:
        cursor.execute(query)
        propiedades = cursor.fetchall()
        
        if not propiedades:
            console.print("[yellow]No hay propiedades en la base de datos.[/yellow]")
            return

        # Creamos la tabla visual con el estilo de Gianfranco
        table = Table(title="🏢 CATÁLOGO INMOBILIARIO", header_style="bold magenta")
        
        table.add_column("Código", style="cyan", justify="center")
        table.add_column("Título", style="white")
        table.add_column("Tipo", style="green")
        table.add_column("Distrito", style="blue")
        table.add_column("Precio", justify="right", style="yellow")
        table.add_column("Estado", justify="center")

        for p in propiedades:
            # Color dinámico según el estado
            color_estado = "green" if p[6] == "disponible" else "red" if p[6] == "vendido" else "yellow"
            
            table.add_row(
                p[0], # codigo_prop
                p[1], # titulo
                p[2], # tipo_prop
                p[3], # distrito
                f"{p[5]} {p[4]:,.2f}", # moneda + precio
                f"[{color_estado}]{p[6]}[/{color_estado}]" # estado con color
            )

        console.print(table)
        
    except sqlite3.Error as e:
        console.print(f"[red]Error al consultar propiedades: {e}[/red]")
    finally:
        conn.close()
        input("\nPresione Enter para continuar...")

def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    dni = input("Número de Documento (DNI): ")
    tipo_doc = "DNI"
    estado = "activo"
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        conn = sqlite3.connect('/workspaces/PythonDatuxBasic/proyecto_v1/bd-si.db')
        cursor = conn.cursor()
        
        query = """
        INSERT INTO clientes (
            nombre, apellido, email, telefono, documento, tipo_doc, 
            direccion, fecha_nacimiento, estado_civil, ingresos, 
            estado, fecha_registro, fecha_actualizacion
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        datos = (
            nombre, apellido, email, telefono, dni, tipo_doc,
            None, None, None, None, # campos NULL en tu imagen
            estado, fecha_hoy, fecha_hoy
        )
        
        cursor.execute(query, datos)
        conn.commit()
        print(f"✅ Cliente {nombre} {apellido} registrado con éxito.")
        
    except sqlite3.Error as e:
        print(f"❌ Error al registrar en la base de datos: {e}")
    finally:
        conn.close()

def resumen_pagos():
    conn = sqlite3.connect('/workspaces/PythonDatuxBasic/proyecto_v1/bd-si.db')
    cursor = conn.cursor()
    
    query = """
    SELECT metodo_pago, SUM(monto), moneda 
    FROM pagos 
    GROUP BY metodo_pago
    """
    
    try:
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        if not resultados:
            console.print("[yellow]No hay registros de pagos para procesar.[/yellow]")
            return

        # Creación de la tabla visual para mostrar el resumen
        table = Table(title="💰 RESUMEN DE PAGOS POR MÉTODO")
        table.add_column("Método de Pago", style="cyan")
        table.add_column("Cantidad Total", justify="right", style="green")
        table.add_column("Moneda", justify="center", style="magenta")

        for metodo, total, moneda in resultados:
            # Formateamos el total con comas para miles y dos decimales
            table.add_row(metodo.capitalize(), f"{total:,.2f}", moneda)

        console.print(table)
        
    except sqlite3.Error as e:
        console.print(f"[red]Error al procesar los pagos: {e}[/red]")
    finally:
        conn.close()
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    try:
        getMenu(conn)
    except KeyboardInterrupt:
        console.print("\n[bold red]Programa interrumpido por el usuario[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
