from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.registro.confirmacion import registroCompleto
from test.registro.registro import registroPruebas
now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " + str(now.minute)

def generar_informe_pdf(nombre_archivo, reporte_registroPruebas, reporte_registroCompleto):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba de registro")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de registro")
    c.drawString(72, 670, reporte_registroPruebas)
    c.drawString(72, 640, reporte_registroCompleto)
    c.save()

def registro():
    resultado_RegistroPruebas = registroPruebas()
    resultado_registro = registroCompleto()
    nombre_archivo = "reportes/registro" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_RegistroPruebas, resultado_registro)

