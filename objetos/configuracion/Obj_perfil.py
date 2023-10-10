from objetos.Obj_home import Ajustes, nombre, apaterno, amaterno, eliminar, cancelar, eliminar2
from objetos.funciones import foto, ruta
Ajustes
nombre
apaterno
amaterno
eliminar
cancelar
eliminar2
subir = '//*[@id="configurator-input-file-upload"]'
foto(subir)
img_path = ruta
print(img_path)
cambiarEmail = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div[2]/div/div/div/div/div/div[2]/span'
newEmail = '//*[@id="emailNew"]'
newEmail2 = '//*[@id="confirmEmail"]'
passEmail = '//*[@id="passwordEmail"]'
mostrarEmail= '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[3]/div/div/div/p'
continuarEmail = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[5]/span[2]'
cancelarEmail = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[5]/span[1]'
cambiarTelefono = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div[3]/div/div/div/div/div/div[2]/span'
cambiarPass = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div[4]/div/div/div/div/div/div[2]/span'
passAnterior = '//*[@id="oldPassword"]'
newPass = '//*[@id="newPassword"]'
cambiarPassword = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[6]/span[2]'
confirmarPassword = '//*[@id="confirmPassWord"]'
CancelarPasseord = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[5]/span[1]'
eliminarCuenta = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div[5]/div/div/div/div/div/div[2]/span'
mostrarPass1 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[1]/div/div/div/p'
mostrarPass2 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[3]/div/div/div/p'
mostrarPass3 = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div[5]/div[1]/div/div/div/p'
telefonoCambio = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div[3]/div/div/div/div/div/div[2]/span'
newTelefono = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/form/div/div/div/input'
cambiarTelefono = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div/span[2]'
cancelarTelefono = '/html/body/app-root/app-dashboard/div/app-configuration-dashboard/div/div/div/div[2]/div/app-configuration-profile/div/div/div/span[1]'
