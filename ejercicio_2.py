def main():
    print("""¿Que conversión desea realizar?
    1) centímetros -> pulgadas
    2) metros -> kilometros
    3) onzas -> gramos
    4) milla -> kilometro
    5) celcius -> fahrenheit
    6) Salir""")
    opcion = int(input("Ingrese una opción: "))
    while opcion > 0 and opcion < 7:
        if opcion == 1:
            conv=float(input("Ingrese la cantidad de centimetros(cm) que desea convertir: "))
            resultado=round((conv/2.54),4)
            print(f"{conv} centimetros es equivalente a {resultado} pulgadas")
        
        elif opcion == 2:
            conv=float(input("Ingrese la cantidad de metros que desea convertir: "))
            resultado=conv/1000
            print(f"{conv} metros es equivalente a {resultado} kilometros")
        
        elif opcion == 3:
            conv=float(input("Ingrese la cantidad de onzas que desea convertir: "))
            resultado=round((conv*28.35),4)
            print(f"{conv} onzas es equivalente a {resultado} gramos")
        
        elif opcion == 4:
            conv=float(input("Ingrese la cantidad de milla que desea convertir: "))
            resultado=round((conv/1.609),4)
            print(f"{conv} millas es equivalente a {resultado} kilometros")
        
        elif opcion == 5:
            conv=float(input("Ingrese la cantidad de celcius que desea convertir: "))
            resultado=round(((conv*(9/5))+32),2)
            print(f"{conv}° celcius es equivalente a {resultado}° fahrenheit") 
        
        else:
            break
        opcion = int(input("Ingrese una opción: "))
        
if __name__ == "__main__":
    main()