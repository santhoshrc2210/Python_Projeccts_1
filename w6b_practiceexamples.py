# Day to number dictionary problem

# Student should enter code below

day_to_number = {'Sunday': 0,"Monday" : 1, "Tuesday": 2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}

# Test data

print day_to_number["Sunday"]
print day_to_number["Monday"]
print day_to_number["Tuesday"]
print day_to_number["Wednesday"]
print day_to_number["Thursday"]
print day_to_number["Friday"]
print day_to_number["Saturday"]

# Sample output

#0
#1
#2
#3
#4
#5
#6

###################################################
# Day to number dictionary problem

# Student should enter code below
name_lookup={"Joe":'Warren',"Scott":'Rixner',"John":'Greiner',"Stephen":'Wong'}

# Test data

print name_lookup["Joe"]
print name_lookup["Scott"]
print name_lookup["John"]
print name_lookup["Stephen"]


# Sample output

#Warren
#Rixner
#Greiner
#Wong

###################################################

# Image debugging problem

# Student should enter code below

import simplegui

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image,test_image_center,test_image_size,test_image_center,test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw)

# start frame
frame.start()
        
###################################################
# Image positioning problem

# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
test_image_size = [95, 93]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]
test_image_pos=test_image_center



# mouseclick handler
def click(pos):
    global test_image_pos
    test_image_pos=pos
    print test_image_pos
    
# draw handler
def draw(canvas):
    global test_image_pos
    canvas.draw_image(test_image,test_image_center,test_image_size,test_image_pos,test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
                                       
