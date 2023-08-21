def main():
    palabra=input("Ingrese una palabra:")
    while palabra != "salir":
        print(palabra[::-1] )
        palabra=input("Ingrese una palabra: ")

    
if __name__ == '__main__':
    main()