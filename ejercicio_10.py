def main():
    lista_compra={}
    total=0
    print("""¿Que operacion desea realizar
          (1)comprar
          (2)salir""")
    opcion=int(input("ingrese una opcion: "))
    while opcion != 2:
        producto= input("ingrese nombre del producto: ")
        lista_compra[producto]=float(input("ingrese el valor del producto: "))
        opcion=int(input("desea seguir comprando (1)Si (2)No \n"))
    print("\n Lista de compra")
    for i in lista_compra:
        print(f"{i}\t{lista_compra[i]}")
        total+=lista_compra[i]
    print("----------------------")
    print(f"Total\t{total}")
    
if __name__ == "__main__":
    main()
        