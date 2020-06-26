# template for "Stopwatch: The Game"
# https://py3.codeskulptor.org/#user305_qXNxlHVKzZ_5.py
import simplegui

# define global variables
ticks=0
a='0'
time='0'
D='0'
attempts_counter='0'
success_attempts=0
total_attempts=0
bug_fix=True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    no_of_seconds=t*0.1
    #calc A
    no_of_minutes=int(no_of_seconds/60)
    A=str(no_of_minutes)
    #calc BC
    BC_int=int(no_of_seconds)-no_of_minutes*60
    if BC_int<10:
        BC='0'+str(BC_int)
    else:
        BC=str(BC_int)
    #calc D
    D_int=no_of_seconds-int(no_of_seconds)
    D_str=str(D_int)
    D=D_str[2]
    time=A+':'+BC+'.'+D

def reflex_test():
    global ticks
    global total_attempts
    global success_attempts
    global attempts_counter
    total_attempts=total_attempts+1
    if ticks%10==0:
        success_attempts= success_attempts+1
    attempts_counter=str(success_attempts)+'/'+str(total_attempts)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global bug_fix
    timer.start()
    bug_fix=True

def stop_button_handler():
    global bug_fix
    timer.stop()
    if bug_fix==True:
        reflex_test()
    bug_fix=False

def reset_button_handler():
    global ticks
    global total_attempts
    global success_attempts
    global attempts_counter
    global a
    timer.stop()
    ticks=0
    a='0'
    success_attempts=0
    total_attempts=0
    attempts_counter='0'


# define event handler for timer with 0.1 sec interval
def tick():
    global ticks
    global a
    ticks=ticks+1
    a=str(ticks)
    return a

# define draw handler
def draw_handler(canvas):
    global ticks
    global time
    format(ticks)
    canvas.draw_text(time, (250, 250), 40, 'Red')
    canvas.draw_text(attempts_counter, (400, 50), 40, 'Green')

# create frame and timer
timer = simplegui.create_timer(100, tick)
frame = simplegui.create_frame("Stop Watch", 500, 500)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button_handler,100)
frame.add_button("Stop", stop_button_handler,100)
frame.add_button("Reset", reset_button_handler,100)


# register event handlers


# start frame and timer
frame.start()

# Please remember to review the grading rubric
