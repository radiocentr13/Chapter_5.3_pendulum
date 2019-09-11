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
    """Function witch paints experimental stand"""
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
    ballradius = 10     #ball radius
    ball = gr.Circle(gr.Point(SIZE_X / 2, SIZE_Y - 2 * rekheight - stickheight), ballradius)
    ball.setFill('yellow')
    ball.draw(window)
    pass


background()
stand()
window.getMouse()
