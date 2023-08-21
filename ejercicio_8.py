def area_circulo():
    radio=int(input("ingrese el radio: "))
    area=3.14*(radio**2)
    return(area)

def vol_cilindro():
    area_ci=area_circulo()
    altura=int(input("ingrese la altura:"))
    volumen=area_ci*altura
    return(volumen)

def main():
    print("""que desea calcular: 
            (1)area circulo
            (2)volumen cilindro
            (3)salir""")
    opcion=int(input("Ingrese una opcion: "))
    while opcion != 3:
        if opcion == 1:
            resultado=area_circulo()
            print("el area del circulo es: "+str(resultado))
        elif opcion == 2:
            resultado=vol_cilindro()
            print("el volumen del cilindro es de: "+str(round(resultado,2)))
        else:
            print("QUE tenga buien dia")
            break
        opcion=int(input("Ingrese una opcion: "))

if __name__ == '__main__':
    main()