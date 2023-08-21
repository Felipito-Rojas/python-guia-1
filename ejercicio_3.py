def main():
    num=int(input("ingrese un numero: "))
    if (num%2 !=0) and (num%3 !=0):
        print("el numero es primo")
    else:
        print("el numero no es primo")
    
if __name__ == "__main__":
    main()