from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.crearVacante.vacante_manual.paso1 import p1
from test.crearVacante.vacante_manual.paso2 import p2
from test.crearVacante.vacante_manual.paso3 import p3
from test.crearVacante.vacante_manual.paso4 import p4
from test.crearVacante.vacante_manual.paso5 import p5
from test.crearVacante.vacante_manual.paso6 import publicarVacante

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)


def generar_informe_pdf(nombre_archivo, reportePaso1, reportePaso2, reportePaso3, reportePaso4,
                        reportePaso5, reportePaso6):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones")
    c.drawString(72, 640, reportePaso1)
    c.drawString(72, 590, reportePaso2)
    c.drawString(72, 570, reportePaso3)
    c.drawString(72, 540, reportePaso4)
    c.drawString(72, 490, reportePaso5)
    c.drawString(72, 470, reportePaso6)
    c.save()


def crearVacante():
    resultado_paso1 = p1()
    resultado_paso2 = p2()
    resultado_paso3 = p3()
    resultado_paso4 = p4()
    resultado_paso5 = p5()
    resultado_paso6 = publicarVacante()
    nombre_archivo = "reportes/CrearVancante" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_paso1, resultado_paso2, resultado_paso3, resultado_paso4, resultado_paso5, resultado_paso6)

