def main():
    numero = int( input("Ingrese un numero: ") )
    factorial = 1
    for n in range(1, numero + 1):
        factorial=factorial*n

    print(factorial)
    
if __name__ == '__main__':
    main()