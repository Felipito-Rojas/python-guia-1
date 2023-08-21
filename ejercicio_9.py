def palabra(lista):
    p_larga=""
    for p in lista:
        if (len(p) > len(p_larga)):
            p_larga = p
    return p_larga

def main():
    lista_palabras=["administracion","recursos","humanos"]
    print(f"la palabra mas larga es: {palabra(lista_palabras)}")
    
if __name__ == '__main__':
    main()