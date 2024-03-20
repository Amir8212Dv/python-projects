from turtle import Turtle
from data import SCREEN_HEIGHT, SCREEN_WIDTH


class Snake:
    def __init__(self):
        self.segments_pos = []
        self.segments = []  # [tale , body , head]
        self.last_removed_tale_pos = None

        for i in range(3):
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

    def update_head_position(self, x_change, y_change):
        """Updates snake's head position and check's if snake is still alive or not and returns the result"""

        self.head_pos = (self.head_pos[0] + x_change, self.head_pos[1] + y_change)
        is_snake_alive = self.check_snake_alive()

        self.segments_pos.append(self.head_pos)
        self.remove_tale()

        return is_snake_alive

    def remove_tale(self):
        """Removes snake tale position and returns it"""

        snake_tale = self.segments_pos[0]
        self.segments_pos.remove(snake_tale)
        self.last_removed_tale_pos = snake_tale

    def check_snake_alive(self):
        if self.head_pos in self.segments_pos:
            return False

        head_hit_the_hor_wall = (SCREEN_WIDTH / 2) - abs(self.head_pos[0]) < 20
        head_hit_the_vrt_wall = (SCREEN_HEIGHT) / 2 - abs(self.head_pos[1]) < 15
        if head_hit_the_hor_wall or head_hit_the_vrt_wall:
            return False

        return True
