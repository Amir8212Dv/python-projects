from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Snake:
    def __init__(self, easyMode: bool):
        self.segments_pos = []
        self.segments = []  # [tale , body , head]
        self.last_removed_tale_pos = None
        self.easyMode = easyMode

        for i in range(15):
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
        """Removes snake tale position and returns it"""

        snake_tale = self.segments_pos[0]
        self.segments_pos.remove(snake_tale)
        self.last_removed_tale_pos = snake_tale

    def check_snake_alive(self):
        if self.head_pos in self.segments_pos:
            injured_segment_index = self.segments_pos.index(self.head_pos) - 1
            self.segments[injured_segment_index].color("red")
            return False

        did_snake_hit_wall = self.check_snake_hit_the_wall()
        if did_snake_hit_wall and not self.easyMode:
            self.segments[-1].color("red")
            return False

        return True

    def check_snake_hit_the_wall(self):
        head_hit_the_vrt_wall = (SCREEN_HEIGHT / 2) - abs(self.head_pos[1]) < 15
        if head_hit_the_vrt_wall:
            if self.easyMode:
                self.head_pos = (self.head_pos[0], (self.head_pos[1] * -1) + 10)
            return True

        head_hit_the_hor_wall = (SCREEN_WIDTH / 2) - abs(self.head_pos[0]) < 20
        if head_hit_the_hor_wall:
            if self.easyMode:
                self.head_pos = ((self.head_pos[0] * -1) + 10, self.head_pos[1])
            return True

        return False

    def move_snake_segments(self):
        for i in range(len(self.segments)):
            self.segments[i].goto(self.segments_pos[i])

        return True
