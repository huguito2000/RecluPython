from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.registro.confirmacion import registroCompleto
now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " +str(now.minute)

def generar_informe_pdf(nombre_archivo, reporteRegistro):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de registro")
    c.drawString(72, 670, reporteRegistro)
    c.save()

if __name__ == '__main__':

    resultado_registro = registroCompleto()
    nombre_archivo = "reportes/informe" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_registro)