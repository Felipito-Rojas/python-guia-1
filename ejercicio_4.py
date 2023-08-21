def main():
    palabra1=input("Ingrese una palabra: ")
    palabra2=input("Ingrese otra palabra para verificar si riman: ")
    if palabra1[-3:] == palabra2[-3:]:
        print(f"{palabra1} y {palabra2} riman")
    elif palabra1[-2:] == palabra2[-2:]:
        print(f"{palabra1} y {palabra2} riman un poco")
    else:
        print(f"{palabra1} y {palabra2} no riman")
    
if __name__ == "__main__":
    main()