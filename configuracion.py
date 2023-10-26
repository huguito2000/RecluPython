from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.configuracion.perfil1 import DatosPerfil
from test.configuracion.empresa2 import SeccionEmpresa
from test.configuracion.facturacion3 import Testfacturacion
from test.configuracion.equipoReclutamiento4 import equipoReclu


now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)


def generar_informe_pdf(nombre_archivo, reporteDatosPerfil, reporteEmpresa, reporteTestfacturacion, reporteEquipoReclu):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas de la configuracion")
    c.drawString(72, 670, reporteDatosPerfil)
    c.drawString(72, 640, reporteEmpresa)
    c.drawString(72, 610, reporteTestfacturacion)
    c.drawString(72, 590, reporteEquipoReclu)

    c.save()


def ajustes():
    resultado_Perfil = DatosPerfil()
    resultado_Empresa = SeccionEmpresa()
    resultado_Facturacion = Testfacturacion()
    resultado_EquipoReclutamiento = equipoReclu()
    nombre_archivo = "reportes/configuracion" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_Perfil, resultado_Empresa, resultado_Facturacion, resultado_EquipoReclutamiento)

