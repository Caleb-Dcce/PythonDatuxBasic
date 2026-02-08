# 3. enviar un email con email.py 
# (ya se encuentra configurado e implementado en login solo cambiar el subject ,mensaje y
# llamarlo en tu funcionalidad implementada)

from config.email import EmailService

def WelcomeCliente(email:str,nombre:str,apellido:str,emailService:EmailService):
    try:
        emailService.send_email(email,"Bienvenido Nuevo Cliente",
        f"Estimado {nombre} {apellido}, A partir de ahora, cuentas con un aliado estratégico para encontrar la propiedad de tus sueños, ya sea tu próximo hogar, oficina o inversión.")
        print("Correo de Bienvenida enviado")
    except Exception as e:
        print("e",e)