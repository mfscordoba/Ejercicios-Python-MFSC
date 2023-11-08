# coding=utf-8
__Author__="Manuel Felipe Sánchez Córdoba"

import webbrowser, urllib.request, urllib.error, urllib.parse

# Programa principal
def main():
    print("MANEJO DE CADENAS")
    print(30*"=")
    nombre=input("Introduzca su nombre: ")
    apellidos=input("Introduzca sus apellidos: ");
    print("¡Hola {0} {1}!".format(nombre,apellidos))
    print("MAYUSCULAS: {0}".format(nombre.upper()))
    print("nombre en minúsculas: "+nombre.lower())

    print("MANEJO DE PÁGINAS WEB")
    print(30*"=")
    url=input("Introduzca URL de la página web: ")
    print("Abriendo página web {0} en una nueva pestaña.".format(url))
    webbrowser.open_new_tab(url)
    
if __name__== "__main__" :
   main()
