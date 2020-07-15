#http://www.codeskulptor.org/#user47_JxT1vbOMDB_8.py
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.set_volume(0.8)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.acceleration=[0,0]
        self.angle = angle
        self.angle_vel = 0
        self.ship_info=info
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        #rotation of ship with left and right keys
        self.angle+= self.angle_vel
        #modular arithematic to update position of ship when out of frame
        if self.pos[0]>=800:
            self.pos[0]=self.pos[0]%800
        elif self.pos[0]<=0:
            self.pos[0]=self.pos[0]+800
        if self.pos[1]>=600:
            self.pos[1]=self.pos[1]%600
        elif self.pos[1]<=0:
            self.pos[1]=self.pos[1]+600
        #updating the position of ship when thrust is on-not accelarating when holding thrust
        if self.thrust:
            forward_vector=angle_to_vector(self.angle)
            self.acceleration=[forward_vector[0],forward_vector[1]]
            self.vel[0]+=1.5*self.acceleration[0]
            self.vel[1]+=1.5*self.acceleration[1]
        #adding friction
        self.vel[0]=0.995*self.vel[0]+self.acceleration[0]
        self.vel[1]=0.995*self.vel[1]+self.acceleration[1]
        #updating pos according to velocity
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]

    def thrust_on(self):
        #image and sound depending on wether thrust
        if self.thrust:
            self.ship_info=ImageInfo([135, 45], [90, 90], 35)
            ship_thrust_sound.play()
        else:
            self.ship_info=ImageInfo([45, 45], [90, 90], 35)
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
        return self.ship_info

    #shooting missile from tip with velocity
    def shoot(self):
        #(self, pos, vel, ang, ang_vel, image, info, sound = None)
        #a_missile = Sprite([self.pos[1], self.pos[1]], [self.vel[0]+1.5*self.acceleration[0],self.vel[1]+1.5*self.acceleration[1]], 0, 0, missile_image, missile_info, missile_sound)
        #return [self.vel[0]+1.5*self.acceleration[0],self.vel[1]+1.5*self.acceleration[1]]
        a=angle_to_vector(2*math.pi-self.angle)
        a_missile.pos= [(self.pos[0]+45)-45*(1-a[0]), self.pos[1]-45*a[1]]
        a_missile.vel= [2*self.vel[0]+20*self.acceleration[0],2*self.vel[1]+20*self.acceleration[1]]
        missile_sound.play()
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]


def draw(canvas):
    global time,lives,score

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)

    canvas.draw_text(('Lives: '+ str(lives)), (50, 30), 25, 'White')
    canvas.draw_text(('Score: '+ str(score)), (650, 30), 25, 'White')


    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()

# timer handler that spawns a rock
def rock_spawner():
    global a_rock
    a1=random.randrange(0, 800, 30)
    a2=random.randrange(0, 600, 25)
    v1=random.randint(-5, 5)
    v2=random.randint(-5, 5)
    a_rock = Sprite([a1, a2], [v1, v2], 0, 0.08, asteroid_image, asteroid_info)

def keydown(key):
    global my_ship,ang_vel
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel=-0.08 #unit of time is 1/60th of a second
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel=0.08
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust=True
        shp_info=my_ship.thrust_on()
        my_ship.update()
        my_ship = Ship(my_ship.pos, my_ship.vel, my_ship.angle, ship_image, shp_info)
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()

def keyup(key):
    global my_ship,ang_vel
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel=0
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel=0
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust=False
        shp_info=my_ship.thrust_on()
        my_ship.update()
        my_ship = Ship(my_ship.pos, my_ship.vel, my_ship.angle, ship_image, shp_info)
    elif key == simplegui.KEY_MAP["space"]:
        pass



# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)


# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [1,0], 0, ship_image, ship_info)
#(self, pos, vel, ang, ang_vel, image, info, sound = None)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.08, asteroid_image, asteroid_info)
a_missile = Sprite([(WIDTH / 2)+45, HEIGHT / 2], [1,0], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
