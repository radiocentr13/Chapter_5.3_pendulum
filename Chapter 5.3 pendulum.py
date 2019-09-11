import graphics as gr
                        #Define window size
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Pendulum 1.0", SIZE_X, SIZE_Y)

def background(color = 'green'):
    """Function paints background
    has 1 input argument - color that is default green"""
    backg = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    backg.setFill(color)
    backg.draw(window)

def stand():
    """Function witch paints experimental stand
        returns coordinates of ball center where thread connects
        center_x, center_y"""
                        #drawing bord
    rekwidth = 400      #bord width
    rekheight = 60      #bord height
    rek = gr.Rectangle(gr.Point(SIZE_X/2 - rekwidth/2, SIZE_Y - rekheight),
                       gr.Point(SIZE_X/2 + rekwidth/2, SIZE_Y - 2*rekheight))
    rek.setFill('brown')
    rek.draw(window)
                        #drawing legs
    legwidth = 15       #leg width
    legheight = 10      #leg height
    leg1 = gr.Rectangle(gr.Point(SIZE_X/2 - rekwidth/2, SIZE_Y - rekheight + legheight),
                        gr.Point(SIZE_X/2 - rekwidth/2 + legwidth, SIZE_Y - rekheight))
    leg1.setFill('grey')
    leg1.draw(window)

    leg2 = gr.Rectangle(gr.Point(SIZE_X/2 + rekwidth/2, SIZE_Y - rekheight + legheight),
                        gr.Point(SIZE_X/2 + rekwidth/2 - legwidth, SIZE_Y - rekheight))
    leg2.setFill('grey')
    leg2.draw(window)
                        #drawing stick
    stickwidth = 4      #stick width
    stickheight = 400   #stick height
    stick = gr.Rectangle(gr.Point(SIZE_X/2 - stickwidth/2, SIZE_Y - 2 * rekheight),
                        gr.Point(SIZE_X/2 + stickwidth/2, SIZE_Y - 2*rekheight - stickheight))
    stick.setFill('black')
    stick.draw(window)

                                #drawing top
    ballradius = 10             #ball radius
    center_x = SIZE_X / 2       #center coordinates
    center_y = SIZE_Y - 2 * rekheight - stickheight
    ball = gr.Circle(gr.Point(center_x, center_y), ballradius)
    ball.setFill('yellow')
    ball.draw(window)
    return center_x, center_y, ballradius
center_x, center_y, rad = stand()
def pendulum(x0 = center_x, y0 = center_y, r = rad):
    l = 350
    rball= 2*rad
    thread = gr.Line(gr.Point(x0, y0 + r), gr.Point(x0, y0 + l))
    thread.setFill('blue')
    thread.draw(window)
    pendball = gr.Circle(gr.Point(x0, y0 + l), rball)
    pendball.setFill('red')
    pendball.draw(window)



print(center_x, center_y)
background()
stand()
pendulum()
window.getMouse()
