import turtle as t, math as m, colorsys as c, random as r

s = t.Screen(); s.setup(600, 600); s.bgcolor("black"); s.tracer(0); t.colormode(255)
p = t.Turtle(); p.hideturtle()

N = 170

def animate(i=0):
    if i >= N: return
    u = i * m.pi * 2 / N
    x = 160 * (m.sin(u) ** 3)
    y = 10 * (13 * m.cos(u) - 5 * m.cos(2*u) - 2 * m.cos(3*u) - m.cos(4*u))
    
    hue = 0.55 + (i / N) * 0.15
    col = [int(v * 255) for v in c.hsv_to_rgb(hue, 0.85, 1)]
    
    p.penup(); p.goto(0, 0); p.pencolor(col); p.pendown(); p.goto(x, y)
    
    for a in range(0, 360, 45):
        p.penup(); p.goto(x, y); p.setheading(a); p.pendown()
        p.fd(r.randint(3, 7))
        
    s.update()
    s.ontimer(lambda: animate(i + 1), 100)

animate()
t.mainloop()