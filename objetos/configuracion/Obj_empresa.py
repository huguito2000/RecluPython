import random
def foto():
    global imagen
    imagen = random.randint(0,10)
    print(imagen)
    return imagen

foto()
logo = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[1]/div/div/div[2]/div/input'
img_path =('/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/Archivos/' + str(imagen) +'.jpeg')
empresa = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[1]/div/div/div/ul/li[2]'
eliminar = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[1]/div/div/div[2]/div/span[2]'
eliminar2 = '/html/body/ngb-modal-window/div/div/div/div[3]/div[2]/button'
cancelar = '/html/body/ngb-modal-window/div/div/div/div[3]/div[1]/button'
nombreEmpresa = '//*[@id="nameCompany"]'
sector = '//*[@id="companySector"]'
giro = '//*[@id="companygiro"]'
tipoEmpresa = '//*[@id="typeCompany"]'
empleados1a10 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[6]/div/div/button[1]'
empleados11a50 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[6]/div/div/button[2]'
empleados50a250 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[6]/div/div/button[3]'
empleados250 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[6]/div/div/button[4]'
pais = '//*[@id="pais"]'
cancelar2 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[8]/span[1]'
actualizar = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-company/div/div/form/div[8]/span[2]'
