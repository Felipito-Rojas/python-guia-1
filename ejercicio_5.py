def main():
    palabra=input("ingrese una palabra: ")
    letra=input("ingrese una letra: ")
    contador=0
    for i in palabra:
        if i == letra:
            contador+=1
    print(contador)
    
    
if __name__ == '__main__':
    main()