def move_forward():
    print("Avanzar")

def rotate_left():
    print("Girar a la izquierda")

def rotate_right():
    print("Girar a la Derecha")



def DoSomething(a):
    for _ in range(a):
        move_forward()


i = 3

for _ in range(3):

    DoSomething(i)
    
    move_forward()

    rotate_right()

    i -= 1


rotate_left()
