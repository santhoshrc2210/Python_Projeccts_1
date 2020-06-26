# implementation of card game - Memory
# http://www.codeskulptor.org/#user47_9dwjn55h5B_3.py

import simplegui
import random

WIDTH=800
HEIGHT=100
lst1=range(8)
lst2=range(8)
lst=lst1+lst2
counter=0
# helper function to initialize globals
def new_game():
    global exposed,counter,state, mem
    state=0
    mem=[]
    random.shuffle(lst)
    counter=0
    exposed=range(16)
    for k in exposed:
        exposed[k]='False'
    label.set_text('Turns= '+str(counter))


# define event handlers
def mouseclick(pos):
    global state,counter
    global i,j
    #game ignores clicks on exposed cards
    if exposed[int(pos[0]/50)]=='False':
    #no cards clicked or all open cards are paired
        if state == 0:
            state = 1
            a=pos[0]/50
            i=int(a)
            mem.append(i)
            exposed[mem[0]]='True'
            counter+=1
    #one card clicked and no cards or cards that are paired are flipped
        elif state == 1:
            b=pos[0]/50
            j=int(b)
            mem.append(j)
            exposed[mem[1]]='True'
            state = 2
    #two cards open and no cards or cards that are paired are flipped
        elif state==2:
            a=pos[0]/50
            k=int(a)
            if lst[mem[0]]!=lst[mem[1]]:
                exposed[mem[0]]='False'
                exposed[mem[1]]='False'
                mem.pop(0)
                mem.pop(0)
                mem.append(k)
                exposed[mem[0]]='True'
                counter+=1
                state = 1
            elif lst[mem[0]]==lst[mem[1]]:
                mem.pop(0)
                mem.pop(0)
                a=pos[0]/50
                i=int(a)
                mem.append(i)
                exposed[mem[0]]='True'
                counter+=1
                state=1
    label.set_text('Turns= '+str(counter))
# cards are logically 50x100 pixels in size
def draw(canvas):
    for k in range(16):
        if exposed[k]=='True':
            canvas.draw_text(str(lst[k]),(50*k+25, HEIGHT/2), 30, 'Red')
    for k in range(16):
        if exposed[k]=='False':
            canvas.draw_polygon([(50*k, 0), (50*(k+1), 0), (50*(k+1), 100),(50*k,100)],
                            2, 'Red','Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns= 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
