from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
from objetos.funciones import click_elemento, text_elemento, captura_time

text_elemento(email, 'huguito.reclutador@yopmail.com', 'login',)
text_elemento(password, 'Abcd.1234', 'login')
click_elemento(BtnContinuar, 'login')
captura_time('login', 2)