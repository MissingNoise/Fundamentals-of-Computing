# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
WIDTH = 300
HEIGHT = 200
stop_counter = 0
correct_stop = 0
correct_color = 'white'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    seconds = float(t * .1)
    minutes = seconds / 60
    if seconds < 10:
        return str(int(minutes)) + ":0" + str(seconds)
    elif seconds < 60:
        return str(int(minutes)) + ":" + str(seconds)
    elif seconds >= 60:
        if seconds - int(minutes) * 60 < 10:
            return str(int(minutes)) + ":0" + str(seconds - int(minutes) * 60)
        else:
            return str(int(minutes)) + ":" + str(seconds - int(minutes) * 60)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global correct_stop, stop_counter, correct_color
    if timer.is_running() == True:
        if time % 10 == 0:
            correct_stop += 1
            correct_color = 'green'
        else:
            correct_color = 'red'
        stop_counter += 1
    timer.stop()

    
def reset():
    global time, correct_stop, stop_counter, correct_color
    time = 0
    correct_stop = 0
    stop_counter = 0
    correct_color = 'white'
    timer.stop()
    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time, correct_color
    time += 1
    correct_color = 'white'


# define draw handler
def draw_handler(canvas):
    canvas.draw_text("Stop at whole second!", (WIDTH/2 - 80, HEIGHT/2 - 40), 20, 'white')
    canvas.draw_text(format(time),(WIDTH/2 - 40, HEIGHT/2 + 20), 40, 'white') 
    canvas.draw_text(str(correct_stop) + "/" + str(stop_counter), (WIDTH - 40, HEIGHT - 170), 20, correct_color)
    
    
# create frame

frame = simplegui.create_frame("Stopwatch: The Game", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.add_button('start', start, 80)
frame.add_button('stop', stop, 80)
frame.add_button('reset', reset, 80)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers


# start frame
frame.start()
# Please remember to review the grading rubric
