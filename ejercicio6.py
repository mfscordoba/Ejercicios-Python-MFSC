# coding=utf-8
__Author__="José Gaspar Sánchez García"


# Función que determina si un numero es primo.

def esPrimo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True



# Programa principal
def main():
    print("ES PRIMO")
    n = int(input("Introduzca un número: "))
    print("{0} es primo --> {1}.".format(n, esPrimo(n)))

if __name__ == "__main__":
    main()
