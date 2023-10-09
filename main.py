from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.Login import loginValido
from test.home import pasa_home, menu, perfil, ajustes

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " +str(now.minute)
def generar_informe_pdf(nombre_archivo, resultado_login, resultado_home, resultado_menu,resultado_perfil, resultado_ajustes):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: "+ fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones")
    c.drawString(72, 670, resultado_login)
    c.drawString(72, 650, resultado_home)
    c.drawString(72, 620, resultado_menu)
    c.drawString(72, 590, resultado_perfil)
    c.drawString(72, 560, resultado_ajustes)

    c.save()

if __name__ == '__main__':
    resultado_login = loginValido()  # Reemplaza esto con la función que obtiene los resultados de tu prueba
    resultado_home = pasa_home()
    resultado_menu = menu()
    resultado_perfil = perfil()
    resultado_ajustes = ajustes()
    nombre_archivo = "reportes/informe"+fecha+".pdf"
    generar_informe_pdf(nombre_archivo, resultado_login, resultado_home, resultado_menu, resultado_perfil,resultado_ajustes)
