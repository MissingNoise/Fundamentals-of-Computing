# implementation of card game - Memory

import simplegui
import random
alist = range(1, 9)
alist.extend(range(1, 9))
c1 = 0
c2 = 0
image = simplegui.load_image('http://i.imgur.com/9LQZ8Fg.jpg')
edd = simplegui.load_image('http://i.imgur.com/sqFVIfF.jpg')
cat = simplegui.load_image('http://i.imgur.com/bGPNx50.png')
rob = simplegui.load_image('http://i.imgur.com/smIkpkP.jpg')
jon = simplegui.load_image('http://i.imgur.com/YS6EAez.jpg')
san = simplegui.load_image('http://i.imgur.com/iTB11CC.jpg')
ary = simplegui.load_image('http://i.imgur.com/phLr8Wn.jpg')
bran = simplegui.load_image('http://i.imgur.com/ygW7Y7G.jpg')
ric = simplegui.load_image('http://i.imgur.com/SodJ2xt.jpg')
stark = {1 : edd, 2 : cat, 3 : rob, 4 : jon, 5 : san, 6 : ary, 7 : bran, 8 : ric}

# helper function to initialize globals

def new_game():
    global exposed, turn, state, color, correct
    random.shuffle(alist)
    exposed = []
    turn = 0
    state = 0
    label.set_text("Turns: " + str(turn))
    for r in range(len(alist)):
        exposed.append(False)
        
def topbot(c):
    """finds the top or bottom and returns given index"""
    if c[1] == 0:
        return c[0]
    else:
        return c[0] + 8

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, turn, state, c1, c2, correct
    card = [pos[0] // 50, pos[1] // 100]
    label.set_text("Turns: " + str(turn))
    if state == 0:
        c1 = topbot(card)
        exposed[topbot(card)] = True
        state = 1
        turn += 1 
    elif state == 1 and not exposed[topbot(card)]:
        c2 = topbot(card)
        exposed[topbot(card)] = True
        state = 2
    elif state == 2 and not exposed[topbot(card)]:
        if alist[c1] != alist[c2]:
            exposed[c1],exposed[c2] = False, False
        exposed[topbot(card)] = True
        c1 = topbot(card)
        state = 1
        turn += 1
                                 
# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(len(alist)):
        if exposed[i] == True:
            if i <= 7:
                """PLEASE COMMENT OUT ALL CANVASE.DRAW_IMAGE IF THEY DON'T LOAD FOR YOU"""
                canvas.draw_text(str(alist[i]),[i * 50 + 15, 65], 40, "White", "sans-serif")
                canvas.draw_image(stark[(alist[i])], (25 , 50), (50, 100), (i * 50 + 25 , 50), (50, 100))
            else:
                canvas.draw_text(str(alist[i]),[(i - 8) * 50 + 15, 165], 40, "White", "sans-serif")
                canvas.draw_image(stark[(alist[i])], (25 , 50), (50, 100), ((i - 8) * 50 + 25 , 150), (50, 100))
        elif exposed[i] == False:
            if i <= 7:
                canvas.draw_polygon([[i * 50, 0], [i * 50 + 50, 0], [i * 50 + 50, 100], [i * 50, 100]], 1, "Black", 'Black')
                canvas.draw_image(image, (i * 50 + 25 , 50), (50, 100), (i * 50 + 25 , 50), (50, 100))
            else:
                canvas.draw_polygon([[(i - 8) * 50, 100], [(i - 8) * 50 + 50, 100], [(i - 8) * 50 + 50, 200], [(i - 8) * 50, 200]], 1, "Black", 'Black')
                canvas.draw_image(image, ((i - 8) * 50 + 25 , 150), (50, 100), ((i - 8) * 50 + 25 , 150), (50, 100))
        if i <= 7:
            canvas.draw_polygon([[i * 50, 0], [i * 50 + 50, 0], [i * 50 + 50, 100], [i * 50, 100]], 1, "Black")
        else:
            canvas.draw_polygon([[(i - 8) * 50, 100], [(i - 8) * 50 + 50, 100], [(i - 8) * 50 + 50, 200], [(i - 8) * 50, 200]], 1, "Black")
                


# create frame and add a button and labels

frame = simplegui.create_frame("Memory", 400, 200)
frame.add_button("Reset", new_game)
label = frame.add_label("Tries: 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric