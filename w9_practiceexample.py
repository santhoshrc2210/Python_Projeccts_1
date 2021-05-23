  def is_stuck(self):
        p=[self.pos[0],0]
        if dist(p,self.pos)<=BUBBLE_RADIUS:
            return True
        else:
            return False
     
 ################################################

def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck
    
    
    
    # update firing angle
    firing_angle += firing_angle_vel
    
    #draw firing line
    orient = angle_to_vector(firing_angle)
    upper_endpoint = [FIRING_POSITION[0] + FIRING_LINE_LENGTH * orient[0], 
                      FIRING_POSITION[1] - FIRING_LINE_LENGTH * orient[1]]
    canvas.draw_line(FIRING_POSITION, upper_endpoint, 4, "White")
    
    # update a_bubble and check for sticking
    a_bubble.update()
    bubble_stuck=a_bubble.is_stuck()
    if bubble_stuck:
        a_bubble=Bubble(firing_sound)
    
    # draw a bubble and stuck bubbles
    a_bubble.draw(canvas)
    
     ################################################

    
