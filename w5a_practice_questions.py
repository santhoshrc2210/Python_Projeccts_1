# Prime number lists

# Student should enter code below
prime_nums_first6=[2,3,5,7,11,13]
print prime_nums_first6[1],prime_nums_first6[3],prime_nums_first6[5]

# Expected output

#3 7 13


###################################################
# Vector addition function

# Student should enter code below
def add_vector(v,w):
    u=list()
    x=v[0]+w[0]
    u.append(x)
    y=v[1]+w[1]
    u.append(y)
    return u

        
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])

# Output

#[4, 3]
#[4, 6]
#[-4, 0]

###################################################

# Mystery bug

# This program should implement two independent timers
# each having their own start and stop buttons.
# Find and correct the error in the code below.

import simplegui

# Initialize two counters.
counter1 = [0, 0]
#counter2=counter1--wrong way to write
counter2 = list(counter1) # correct way list referencing


# Define event handlers.
def start1():
    timer1.start()
    
def stop1():
    timer1.stop()
    
def start2():
    timer2.start()
    
def stop2():
    timer2.stop()
    
def tick1():
    global counter
    if counter1[1] == 9:
        counter1[0] += 1
        counter1[1] = 0
    else:
        counter1[1] += 1

def tick2():
    global counter
    if counter2[1] == 9:
        counter2[0] += 1
        counter2[1] = 0
    else:
        counter2[1] += 1
        
        
# Define draw handler.
def draw(canvas):
    canvas.draw_text("Timer 1:     " + str(counter1[0] % 10) + "." + str(counter1[1]), [50, 100], 24, "White")
    canvas.draw_text("Timer 2:     " + str(counter2[0] % 10) + "." + str(counter2[1]), [50, 200], 24, "White")

# Register event handlers.
frame = simplegui.create_frame("Mystery bug", 300, 300)
frame.add_button("Start timer1", start1, 200)
frame.add_button("Stop timer1", stop1, 200)
frame.add_button("Start timer2", start2, 200)
frame.add_button("Stop timer2", stop2, 200)
frame.set_draw_handler(draw)

timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)


# Start frame.
frame.start()



