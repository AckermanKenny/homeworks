import turtle as ben_and_ben   #Credits to Amuls Academy, Rajesh Alane

araw_araw = 50
ben_and_ben.bgcolor("plum")
ben_and_ben.color("purple")
ben_and_ben.width(5)
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,100)
ben_and_ben.pendown()
ben_and_ben.circle(-120,steps=3)
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,-140)
ben_and_ben.pendown()
ben_and_ben.circle(120,steps=3)

pagtingin = -150
make_it_with_you = 130
ben_and_ben.width(6)
ben_and_ben.color("black")
ben_and_ben.width(2)
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,pagtingin)
ben_and_ben.pendown()
ben_and_ben.circle(make_it_with_you)
ben_and_ben.begin_fill()
ben_and_ben.fillcolor("purple")
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,-75)
ben_and_ben.pendown()
ben_and_ben.circle(55)
ben_and_ben.end_fill()
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,-155)
ben_and_ben.pendown()
ben_and_ben.circle(135)
ben_and_ben.width(6)
ben_and_ben.color("purple")
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,-300)
ben_and_ben.pendown()
ben_and_ben.circle(280)
ben_and_ben.width(2)
ben_and_ben.color("black")
ben_and_ben.penup()
ben_and_ben.goto(araw_araw,-320)
ben_and_ben.pendown()
ben_and_ben.circle(300)
ben_and_ben.penup()
ben_and_ben.goto(-90,-195)
ben_and_ben.pendown()
talaarawan = 90
paalam = 350
for i in range(5):
    for colors in ("red", "black", "black", "red", "red"):
        ben_and_ben.speed(0)
        ben_and_ben.color(colors)
        ben_and_ben.pensize(6)
        ben_and_ben.left(12)
        ben_and_ben.forward(paalam)
        ben_and_ben.left(talaarawan)
        ben_and_ben.forward(paalam)
        ben_and_ben.left(talaarawan)
        ben_and_ben.forward(paalam)
        ben_and_ben.left(talaarawan)
        ben_and_ben.forward(paalam)
        ben_and_ben.left(talaarawan)
        ben_and_ben.forward(paalam)
        ben_and_ben.left(talaarawan)
ben_and_ben.done()
