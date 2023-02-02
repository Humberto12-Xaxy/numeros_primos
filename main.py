def primos(n):

    contador = 0
    lista_contador = []
    for i in range(1, n+1):
        contador = 0
        for j in range(1, n+1):
            if i % j == 0 and i % 1 == 0:
                contador += 1          
        lista_contador.append(contador)

    for indice, numero in enumerate(lista_contador):
        if numero < 3:
            print(indice +1 )

if __name__ == '__main__':
    primos(20)