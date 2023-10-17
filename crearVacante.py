from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.crearVacante.vacante_manual.paso6 import publicarVacante

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " + str(now.minute)

def generar_informe_pdf(nombre_archivo, reporteCrearVacante):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones")
    c.drawString(72, 670, reporteCrearVacante)
    c.save()

if __name__ == '__main__':
    def crearVacante():
        resultado_crearVacante = publicarVacante()
        nombre_archivo = "reportes/informe" + fecha + ".pdf"
        generar_informe_pdf(nombre_archivo, resultado_crearVacante)