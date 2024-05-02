import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_RADIUS = 15
BALL_SPEED = 3


class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, color, sound_file):
        """ Constructor. """
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color
        self.sound = arcade.Sound(sound_file)

    def draw(self):
        """ Draw the ball with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, BALL_RADIUS, self.color)

    def update(self):
        """ Update the ball's position and direction. """
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Check for collisions with screen edges
        if self.position_x < BALL_RADIUS or self.position_x > SCREEN_WIDTH - BALL_RADIUS:
            self.change_x *= -1
            self.sound.play(volume=0.1)  # Play sound when hitting the screen edge
        if self.position_y < BALL_RADIUS or self.position_y > SCREEN_HEIGHT - BALL_RADIUS:
            self.change_y *= -1
            self.sound.play(volume=0.1)  # Play sound when hitting the screen edge


class Square:
    """ This class manages a square moving on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, color):
        """ Constructor. """
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        """ Draw the square with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, BALL_RADIUS * 2, BALL_RADIUS * 2, self.color)

    def update(self):
        """ Update the square's position and direction. """
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Check for collisions with screen edges
        if self.position_x < BALL_RADIUS or self.position_x > SCREEN_WIDTH - BALL_RADIUS:
            self.change_x *= -1
        if self.position_y < BALL_RADIUS or self.position_y > SCREEN_HEIGHT - BALL_RADIUS:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """ Initialize the game. """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Load background image
        self.background = arcade.load_texture("bg.jpg")

        # Create a list for the balls
        self.balls = [
            Ball(50, 50, BALL_SPEED, BALL_SPEED, arcade.color.AUBURN, ":resources:sounds/upgrade4.wav")
            for _ in range(3)
        ]

        # Create a square
        self.square = Square(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50, -BALL_SPEED, -BALL_SPEED, arcade.color.BLIZZARD_BLUE)

    def on_draw(self):
        """ Draw everything in the game. """
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        for ball in self.balls:
            ball.draw()
        self.square.draw()

    def on_update(self, delta_time):
        """ Update the game logic. """
        for ball in self.balls:
            ball.update()
        self.square.update()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.run()


if __name__ == "__main__":
    main()
