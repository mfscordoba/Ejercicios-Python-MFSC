"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "))
    
    if edad <18:
        print(f'{nombre}, eres menor de edad no puedes conducir')
    else:
        print(f'{nombre}, tu edad te permite conducir, felicidades')

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es nayor de edad
    # Sino --> Todavía eres menor de edad

if __name__== "__main__" :
    main()
