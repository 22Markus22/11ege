from turtle import *

def n1():
    screensize(10_000, 10_000)
    tracer(0)
    lt(90)
    m = 10

    for i in range(2):
        fd(10 * m)
        rt(90)
        fd(20 * m)
        rt(90)

    up()
    fd(3 * m)
    rt(90)
    fd(7 * m)
    lt(90)
    down()

    for i in range(2):
        fd(70 * m)
        rt(90)
        fd(90 * m)
        rt(90)

    for x in range(7, 21):
        for y in range(3, 11):
            teleport(x*m,y*m)
            dot(3, 'red')
    answ = (21-7)*(11-3)
    update()
    print(answ)
    done()

def n2():
    screensize(10_000, 10_000)
    tracer(0)
    lt(90)
    m = 10

    for i in range(2):
        fd(13 * m)
        rt(90)
        fd(20 * m)
        rt(90)

    up()
    fd(8 * m)
    rt(90)
    bk(3 * m)
    lt(90)
    down()

    for i in range(2):
        fd(16 * m)
        rt(90)
        fd(8 * m)
        rt(90)

    for x in range(0, 6):
        for y in range(8, 14):
                teleport(x * m, y * m)
                dot(3, 'red')

    print((13*20)+(16*8)-(6*6))
    update()
    done()

def n3():
    screensize(10_000, 10_000)
    tracer(0)
    lt(90)
    m = 10

    for i in range(3):
        fd(39*m)
        rt(90)
        fd(48*m)
        rt(90)
    penup()

    fd(27*m)
    rt(90)
    fd(24*m)
    lt(90)

    pendown()

    for i in range(3):
        fd(29*m)
        rt(90)
        bk(18*m)
        rt(90)

    for x in range(24, 43):
            for y in range(0, 13):
                    teleport(x * m, y * m)
                    dot(3, 'red')


    update()
    print((39*48)+(29*18)-(19*13))
    done()

def N6019():
    screensize(10_000, 10_000)
    tracer(0)
    lt(90)
    m = 10
    for i in range(2):
        fd(21*m)
        rt(90)
        fd(27*m)
        rt(90)
    penup()
    fd(9*m)
    rt(90)
    fd(10*m)
    lt(90)
    pendown()
    for i in range(2):
        fd(86*m)
        rt(90)
        fd(47*m)
        rt(90)
    for x in range(10, 28):
            for y in range(9, 22):
                    teleport(x * m, y * m)
                    dot(3, 'red')
    print(18*13)
    update()
    done()

def N6030():
    screensize(10_000, 10_000)
    tracer(0)
    lt(90)
    m = 10
    for i in range(2):
        fd(28*m)
        rt(90)
        fd(18*m)
        rt(90)
    penup()
    fd(14*m)
    rt(90)
    fd(10*m)
    rt(90)
    pendown()
    for i in range(2):
        fd(30*m)
        rt(90)
        fd(7*m)
        rt(90)
    update()
    

