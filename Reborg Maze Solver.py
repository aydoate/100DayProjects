#define actions
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def navigate():
    while wall_on_right():               #Check to see if wall is on right 
        if  front_is_clear():            #if front is clear, move ahead
            move()
        elif wall_in_front():            #if wall in front, turn left and go back to while loop
            turn_left()
    else:
        if at_goal():                   #check to see if at goal line, if not
            done()
        else:                           #if not at goal line, Reborg must be at a corner of either 90 or 180 degrees
            turn_right()                #begin turning corner
            move()                      #move one step
            if wall_on_right():         #if a 90 degree turn, move back to navigate loop
                navigate()
            else:                       #if a 180 degree turn, turn right and move one extra step, then back to navigate loop
                turn_right()
                move()
                navigate()
   
#start code
while not wall_in_front():             #move forward until find initial wall
    move()
else:                                  #once wall is found, turn left and beguin navigate while loop
    turn_left()
    navigate()
