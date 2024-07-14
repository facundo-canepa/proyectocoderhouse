def mensaje():
    print("estoy trabajando con git")
    mensaje()

def sumar(n1,n2):
    print("el resultado de la suma entre n1 + n2: ", n1 + n2)
    
    sumar(int(input("Ingresa el primer número: ")),int(input("Ingresa el segundo número: ")))