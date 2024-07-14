def mensaje():
    print("estoy trabajando con git")
    mensaje()

def sumar(n1,n2):
    print("el resultado de la suma entre n1 + n2: ", n1 + n2)
    
    sumar(int(input("Ingresa el primer número: ")),int(input("Ingresa el segundo número: ")))

def multiplicar(n1,n2):
    print("el resultado de la multiplicación entre n1 * n2: ", n1 * n2)
    
    multiplicar(int(input("Ingresa el primer número: ")),int(input("Ingresa el segundo número: ")))

def mensaje3():
    print("Estoy en la rama facundo.canepa ahora con github")