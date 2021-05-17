#Practice questions Week 4
# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)
frame.start()

###################################################
# Display "This is easy?"
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text('This is easy?', (20, 20), 12, 'Red')
    
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
###################################################

# Display an X
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw_handler(canvas):
    canvas.draw_text('X', (5, 40), 48, 'Red')
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('Testing', 96, 96)
frame.set_draw_handler(draw_handler)
frame.start()

# Start the frame animation
###################################################
# Define a function that returns formatted minutes and seconds


# Time formatting function
# Student should enter function on the next lines.
def format_time(tot_seconds):
    minutes=tot_seconds//60
    seconds=tot_seconds%60
    ans= str(minutes)+' minutes and '+str(seconds)+' seconds'
    return ans

# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds

###################################################
# Move a ball
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw_handler(canvas):
    canvas.draw_circle((HEIGHT/2, WIDTH/2), ball_radius, 5, 'Green')
    
# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius +=RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    if ball_radius>RADIUS_INCREMENT:
        ball_radius -=RADIUS_INCREMENT
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()



