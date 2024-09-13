import turtle

def draw_heart(t, size, color):
    t.begin_fill()
    t.color(color)
    t.left(140)
    t.forward(size)

    t.circle(-size // 2, 200)

    t.left(120)
    t.circle(-size // 2, 200)

    t.forward(size)
    t.end_fill()
    t.setheading(0)

def draw_hearts():
    screen = turtle.Screen()  # Instância de Screen
    screen.bgcolor('lightpink')  # Definindo a cor de fundo
    t = turtle.Turtle()
    t.speed(3)
    t.width(3)

    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#E793A2', '#DC8788', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors):
        t.penup()
        t.goto(0, -size // 2)
        t.pendown()
        draw_heart(t, size, color)

    t.hideturtle()
    screen.mainloop()  # Manter a tela aberta

draw_hearts()