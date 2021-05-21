# Use of Person class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)

# Student adds code where appropriate    
    
# implementation of average_age
def average_age(person_list, current_year):
    sum_age=0
    for i in person_list:
        sum_age+=i.age(current_year)
    avg_age=float(sum_age)/len(person_list)
    return avg_age
    
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

instructors = [joe, john, stephen, scott]
print average_age(instructors, 2013)

instructors.pop() # get rid of Scott and his bogus age
print average_age(instructors, 2013)

# Output of testing code 

#44.5
#50.6666666667

#################################################
# Implementation of Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)

# Student adds code where appropriate

# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.password=pwd
        self.person=person
        self.project_list=[]
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        if self.password==pwd:
            return True
        elif self.password!=pwd:
            return False
    
    def get_projects(self):
        return self.project_list
    
    def add_project(self, project):
        self.project_list.append(project)
        
 # Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()

# Output of testing code 

#Joe Warren
#False
#True
#[]
#['Create practice exercises']
#['Create practice exercises', 'Implement Minecraft']

# Use of the Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)


# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
        
# Student adds code where appropriate
        
# definition of function assign
def assign(students, name, pwd, project): 
    for student in students:
        if student.get_name()==name and student.check_password(pwd):
            if project not in student.get_projects():
                student.add_project(project)

    
 
# Testing code

# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()


# Output of testing code 

#['Create practice exercises', 'Implement Minecraft']
#['Create practice exercises', 'Implement Minecraft', 'Practice RiceRocks']
#[]
#[]
#['Work on reflexes']

#################################################

# Initialize a game of Memory using the Tile class

# Student adds code where appropriate    

import simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    # add code here
    list_1=range(0, DISTINCT_TILES)
    random.shuffle(list_1)
    list_2=range(0, DISTINCT_TILES)
    random.shuffle(list_2)
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     
       
            
# draw handler
def draw(canvas):
    for tile in tile_list:
        tile.draw_tile(canvas)
        
    # add code here

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
    
    
# Create a horizontal row of 16 Memory tile with numbers hidden
tile_list=[]
for i in range(2 * DISTINCT_TILES):
    tile_list.append(Tile(i,False,[TILE_WIDTH*i,TILE_HEIGHT]))

#################################################

 # Build clickable version of Memory using the Tile class

# Student adds code where appropriate    

import simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    tile_numbers = range(DISTINCT_TILES) * 2
    random.shuffle(tile_numbers)
    my_tiles = [Tile(tile_numbers[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]
    
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     
        

# define event handlers
def mouseclick(pos):
    # add code here
    tile_ind=pos[0]/TILE_WIDTH
    print tile_ind
    my_tiles[tile_ind].expose_tile()
    
            
# draw handler
def draw(canvas):
    for tile in my_tiles:
        tile.draw_tile(canvas)
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)


# get things rolling
new_game()
frame.start()
    
 # Clicking on tile should flip them once
 
###################################################










