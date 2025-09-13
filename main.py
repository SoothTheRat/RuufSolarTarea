

def max_paneles(X, Y, a, b):
    def contar(x, y, a, b):
        
        filas = x // a
        cols = y // b
        total = filas * cols

        sobra_x = x - filas * a
        if sobra_x >= b:
            total += (sobra_x // b) * (y // a)

        sobra_y = y - cols * b
        if sobra_y >= a:
            total += (sobra_y // a) * (x // b)

        return total

    return max(contar(X, Y, a, b), contar(X, Y, b, a))


print("=== Calculadora de paneles solares ===")
X = int(input("Ingresa el ancho del techo (X): "))
Y = int(input("Ingresa el alto del techo (Y): "))
a = int(input("Ingresa el ancho del panel (a): "))
b = int(input("Ingresa el alto del panel (b): "))

resultado = max_paneles(X, Y, a, b)
print(f"\nMáxima cantidad de paneles que caben: {resultado}")