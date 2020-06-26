#rock paper lizard spock scissors function
#run in codeskulptor

def name_to_number(name):
    if name=='rock':
       return 0
    elif name=='Spock':
       return 1
    elif name=='paper':
       return 2
    elif name=='lizard':
       return 3
    elif name=='scissors':
       return 4
    else:
       a= 'Error: Wrong invalid input'
       return a

def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        a1= 'Error: Wrong invalid input'
        return a1

def rpsls(player_choice):
    print('\nPlayer chooses '+player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print('Computer chooses '+comp_choice)
    x=comp_number-player_number
    y=x%5
    if y==4 or y==3:
       print('Player wins!')
    elif y==1 or y==2:
       print('Computer wins!')
    else:
       print('Player and Computer tie!')

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
