# Circle clicking problem

###################################################
# Student should enter code below

import simplegui
import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    red_dist=dist(pos,RED_POS)
    green_dist=dist(pos,GREEN_POS)
    blue_dist=dist(pos,BLUE_POS)
    if red_dist<RADIUS:
        print 'Red ball clicked'
    elif green_dist<RADIUS:
        print 'Green ball clicked'
    elif  blue_dist<RADIUS:
        print 'Blue ball clicked'
          

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


# Sample output

#Clicked red ball
#Clicked green ball
#Clicked blue ball
#Clicked green ball
#Clicked red ball
#Clicked green ball
#Clicked blue ball

###################################################

# Day to number problem

# Student should enter code below

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    pos=day_list.index(day)
    return pos
    
# Test data

print day_to_number("Sunday")
print day_to_number("Monday")
print day_to_number("Tuesday")
print day_to_number("Wednesday")
print day_to_number("Thursday")
print day_to_number("Friday")
print day_to_number("Saturday")

# Sample output

#0
#1
#2
#3
#4
#5
#6

###################################################
# String list joining problem

# Student should enter code below

def string_list_join(string_list):
    concat_str=''
    for strng in string_list:
        concat_str+=strng
    return concat_str    

# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


# Output

#
#pigdog
#spam and eggs
#abcd
###################################################

# Ball grid solution

# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    center_point=[BALL_RADIUS,BALL_RADIUS]
    for j in range(10):
        center_point[1]=(2*j+1)*BALL_RADIUS
        for i in range(10):
            center_point[0]=(2*i+1)*BALL_RADIUS
            canvas.draw_circle(center_point, BALL_RADIUS, 2, 'RED')
           
     
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

###################################################
# Student should enter code below
# Polyline drawing problem


import simplegui
import math

polyline = []
click_ctr=0
point=[]
# define mouseclick handler
def click(pos):
    global click_ctr,point
    click_ctr+=1
    if click_ctr==1:
        point=(pos)
    elif click_ctr==2:
        point=list(point)
        point.append(pos)
        a=point.pop(0)
        b=point.pop(0)
        p=(a,b)
        point.insert(0,p)
    elif click_ctr>=3:
        point.append(pos)
    return point
          
# button to clear canvas
def clear():
    global click_ctr,point
    click_ctr=0

# define draw
def draw(canvas):
    global click_ctr,point
    if click_ctr==1:
        canvas.draw_point(point, 'Green')
    elif click_ctr>=2:
        canvas.draw_polyline(point, 5, 'Red')
    elif click_ctr==0:
        canvas.draw_polygon([(0, 0), (0, 300), (300, 300), (300,0)], 12, 'Black','Black')

                          
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()


