# Implementation of classic arcade game Pong
# https://py3.codeskulptor.org/#user305_kWWAKvA8Ko_1.py
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=0
score_left=0
score_right=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel,HEIGHT,BALL_RADIUS # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction==RIGHT:
        ball_vel[0]=2
        ball_vel[1]=-2
    elif direction==LEFT:
        ball_vel[0]=-2
        ball_vel[1]=-2

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_left, score_right  # these are ints
    score_left=0
    score_right=0
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    spawn_ball(RIGHT)


def draw(canvas):
    global score_left, score_right, paddle1_pos, paddle2_pos, ball_pos, ball_ve, HEIGHT,BALL_RADIUS, PAD_WIDTH, paddle1_vel, paddle2_vel

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos>PAD_HEIGHT/2 and paddle1_pos<HEIGHT-(PAD_HEIGHT/2):
        paddle1_pos+=paddle1_vel
    elif paddle1_pos<=PAD_HEIGHT/2 :
        paddle1_pos+=1
    elif paddle1_pos>=HEIGHT-(PAD_HEIGHT/2):
        paddle1_pos-=1
    if paddle2_pos>PAD_HEIGHT/2 and paddle2_pos<HEIGHT-(PAD_HEIGHT/2) :
        paddle2_pos+=paddle2_vel
    elif paddle2_pos<=PAD_HEIGHT/2:
        paddle2_pos+=1
    elif paddle2_pos>=HEIGHT-(PAD_HEIGHT/2):
        paddle2_pos-=1

    # determine whether paddle and ball collide
    if ball_pos[0]==BALL_RADIUS+PAD_WIDTH and ball_pos[1]<=paddle1_pos+PAD_HEIGHT/2 and  ball_pos[1]>=paddle1_pos-PAD_HEIGHT/2 :
        ball_vel[0]=-ball_vel[0]
    elif ball_pos[0]==WIDTH-BALL_RADIUS-PAD_WIDTH and ball_pos[1]<=paddle2_pos+PAD_HEIGHT/2 and  ball_pos[1]>=paddle2_pos-PAD_HEIGHT/2:
        ball_vel[0]=-ball_vel[0]
    elif ball_pos[0]==BALL_RADIUS:
        score_right+=1
        spawn_ball(RIGHT)
    elif ball_pos[0]==WIDTH-BALL_RADIUS:
        score_left+=1
        spawn_ball(LEFT)

    # update ball
    if ball_pos[1]==BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]==HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "RED", "White")
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-PAD_HEIGHT/2 ], [PAD_WIDTH,paddle1_pos-PAD_HEIGHT/2 ], [PAD_WIDTH,paddle1_pos+PAD_HEIGHT/2 ],[0,paddle1_pos+PAD_HEIGHT/2 ]], 1,'Blue', 'WHITE')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos-PAD_HEIGHT/2 ], [WIDTH,paddle2_pos-PAD_HEIGHT/2 ], [WIDTH,paddle2_pos+PAD_HEIGHT/2 ], [WIDTH-PAD_WIDTH,paddle2_pos+PAD_HEIGHT/2 ]], 1,'Blue', 'WHITE')
    # draw scores
    canvas.draw_text(str(score_left), ((WIDTH / 2)-20, 30), 30, 'Green')
    canvas.draw_text(str(score_right), ((WIDTH / 2)+10, 30), 30, 'Green')

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel-=3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel+=3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel-=3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel+=3


def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)
frame.add_button("Restart", new_game,100)


# start frame
new_game()
frame.start()
