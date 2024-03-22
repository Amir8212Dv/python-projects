from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Snake:
    def __init__(self, easyMode: bool):
        self.segments_pos = []
        self.segments = []  # [tale , body , head]
        self.last_removed_tale_pos = None
        self.easyMode = easyMode
        self.initial_segments_count = 3

        for i in range(self.initial_segments_count):
            self.generate_new_segment(backward=i * 20)
        self.head_pos = self.segments_pos[-1]

    def generate_new_segment(self, backward: int = 0):
        segment = Turtle("square")
        segment.color("white")
        segment.pu()

        if backward:
            segment.backward(backward)
        elif self.last_removed_tale_pos:
            segment.goto(self.last_removed_tale_pos)

        self.segments.insert(0, segment)
        self.segments_pos.insert(0, segment.pos())

    def move(self, move_steps):
        """Move snake body and update positions and check if snake is still alive or not and return the result"""

        self.head_pos = (self.head_pos[0] + move_steps[0], self.head_pos[1] + move_steps[1])
        is_snake_alive = self.check_snake_alive()

        self.segments_pos.append(self.head_pos)
        self.remove_tale()

        self.move_snake_segments()

        return is_snake_alive

    def remove_tale(self):
        """Removes snake tale position and saves the position in attribute"""

        snake_tale = self.segments_pos[0]
        self.segments_pos.remove(snake_tale)
        self.last_removed_tale_pos = snake_tale

    def check_snake_alive(self):
        if len(self.segments) > self.initial_segments_count and self.head_pos in self.segments_pos[:-1]:
            return False

        did_snake_hit_wall = self.check_snake_hit_the_wall()
        if did_snake_hit_wall and not self.easyMode:
            return False

        return True

    def check_snake_hit_the_wall(self):
        head_hit_the_vrt_wall = (SCREEN_HEIGHT / 2) - abs(self.head_pos[1]) < 15
        if head_hit_the_vrt_wall:
            if self.easyMode:  # In easy mode teleport snake to the other side's wall
                old_y = self.head_pos[1]
                new_y = (old_y * -1) + (50 * (old_y / abs(old_y)))  # f(Y)= -Y + (50Y / |Y|)
                self.head_pos = (self.head_pos[0], new_y)
            return True

        head_hit_the_hor_wall = (SCREEN_WIDTH / 2) - abs(self.head_pos[0]) < 20
        if head_hit_the_hor_wall:
            if self.easyMode:  # In easy mode teleport snake to the other side's wall
                old_x = self.head_pos[0]
                new_x = (old_x * -1) + (50 * (old_x / abs(old_x)))  # f(X)= -X + (50X / |X|)
                self.head_pos = (new_x, self.head_pos[1])
            return True

        return False

    def move_snake_segments(self):
        for i in range(len(self.segments)):
            self.segments[i].goto(self.segments_pos[i])

        return True

    def game_over(self):
        for segment in self.segments:
            segment.goto(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)  # Put the dead snake out of screen
        self.segments.clear()
        self.segments_pos.clear()
