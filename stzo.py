def move_forward():
    print("Avanzar")

def rotate_left():
    print("Girar a la izquierda")# Definir la función ComboMove

def rotate_right():
    print("Girar a la Derecha")
# Definir la función FancyMove

# Definir la función DoSomething
def DoSomething(a):
    for _ in range(a):
        move_forward()

# Inicializar i a 3
i = 3

# Repetir 3 veces
for _ in range(3):
    # Llamar a la función DoSomething con el valor de i
    DoSomething(i)
    
    # Mover hacia adelante
    move_forward()
    
    # Girar a la derecha
    rotate_right()
    
    # Decrementar i en 1
    i -= 1

# Girar a la izquierda
rotate_left()
