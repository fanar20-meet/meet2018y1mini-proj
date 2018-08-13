import turtle
import random #We'll need this later in the lab
import time
cube = turtle.clone()
cube.hideturtle()
cube.penup()
cube.goto(300,300)
cube.pendown()
cube.goto(300,-300)
cube.goto(-300,-300)
cube.goto(-300,300)
cube.goto(300,300)

screen = turtle.Screen()





turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=650
SIZE_Y=650
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("arrow")
snake.color('red')

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for sn in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    IDstamp = snake.stamp()
    stamp_list.append(IDstamp)


UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    
    #Update the snake drawing <- remember me later
    print("You pressed the up key!")
def down():
    global direction
    direction=DOWN
    
    print("you pressed the down key!")
def left():
    global direction
    direction=LEFT
    
    print("you pressed the left key!")
def right():
    global direction 
    direction = RIGHT
    
    print("you pressed the right key!")
snake.color('yellow')
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)

turtle.listen()


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    stamp_ID = food.stamp()
    food_stamps.append(stamp_ID)

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

    



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    global direction
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("you moved down!")
        
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)



    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]


    if snake.pos() in pos_list[:-1]:
        print("you ate yourself ! Game over!")
        quit()
       
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    #HINT: This if statement may be useful for Part 8
    
    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
#turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function


# The next three lines check if the snake is hitting the 
# right edge.


    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("you hit the up edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! Game over!")
        screen.bgpic("GO.gif")
        screen.update()
        time.sleep(2)
        quit()

    turtle.ontimer(move_snake,TIME_STEP)


turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script


food = turtle.clone()
food.shape("trash.gif")
food.hideturtle()

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
snake.color("blue")
for this_food_pos in food_pos :


    food.goto(this_food_pos)

    stamp_ID = food.stamp()
    food_stamps.append(stamp_ID)
   
move_snake()

