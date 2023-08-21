def main():
    import random
    num=int(random.randrange(1, 100))
    print(num)
    
    jugador=int(input("Ingrese un posible numero(0-100): "))
    while jugador != num and ((jugador < 100) or (jugador > 0)):
        if jugador > num:
            print("muy alto")
        elif jugador < num:
            print("muy bajo")
        else:
            print("correcto")
        jugador=int(input("Ingrese un posible numero(0-100): "))
    print("felicidades ganaste")
    
        
if __name__ == "__main__":
    main()