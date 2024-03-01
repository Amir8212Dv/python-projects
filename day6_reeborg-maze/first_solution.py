
#! Game URL : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# * I wrote this solution by my self, and compared to the second solution which i copied from tutorial, this one is 4 lines longer, but instead, this one is more faster in problem_world files

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not is_facing_north():
    turn_left()

turn_right_in_row = 0

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if turn_right_in_row >= 4:
            move()
            turn_right_in_row = 0
        else:
            turn_right_in_row += 1
    else:
        turn_left()
        turn_right_in_row = 0
