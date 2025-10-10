def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        jump_down()
    else:
        jump()
        
def jump_down():
    if front_is_clear():
        move()
        jump_down()
    else:
        turn_left()
        run()
        
def run():
    while not at_goal():
        if wall_in_front():
            turn_left()
            jump()
        else:
            move()
            
run()
