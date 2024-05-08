import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

#  ====================== ROCKET ===========================>

class Rocket:
    def __init__(self, image_file, size):
        self.image = arcade.Sprite(image_file, size)
        self.speed = MOVEMENT_SPEED

    def draw(self):
        self.image.draw()

    def update(self):
        self.image.center_x += self.image.change_x
        self.image.center_y += self.image.change_y
        self.image.change_x = 0
        self.image.change_y = 0

    def update_with_keyboard(self, key_list):
        if key_list.get(arcade.key.UP, False):
            self.image.change_y = self.speed
        elif key_list.get(arcade.key.DOWN, False):
            self.image.change_y = -self.speed
        else:
            self.image.change_y = 0

        if key_list.get(arcade.key.LEFT, False):
            self.image.change_x = -self.speed
        elif key_list.get(arcade.key.RIGHT, False):
            self.image.change_x = self.speed
        else:
            self.image.change_x = 0

    def update_with_mouse(self, x, y):
        self.image.center_x = x
        self.image.center_y = y

# ====================================== Moving Ball =============================>

class MovingCircle:
    def __init__(self, radius):
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.radius = radius
        self.change_x = MOVEMENT_SPEED
        self.change_y = MOVEMENT_SPEED
        self.hit_sound = arcade.Sound(":resources:sounds/upgrade4.wav")

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.RED)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x <= self.radius or self.center_x >= SCREEN_WIDTH - self.radius:
            self.change_x *= -1
            self.hit_sound.play(volume=0.1)

        if self.center_y <= self.radius or self.center_y >= SCREEN_HEIGHT - self.radius:
            self.change_y *= -1
            self.hit_sound.play(volume=0.1)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.background = arcade.load_texture("bg.jpg")
        self.key_list = None

        # Initialize rockets
        self.rocket1 = Rocket("rocket1.png", 0.05)
        self.rocket1.image.center_x = SCREEN_WIDTH // 3
        self.rocket1.image.center_y = SCREEN_HEIGHT // 3

        self.rocket2 = Rocket("rocket2.png", 0.1)
        self.rocket2.image.center_x = SCREEN_WIDTH // 2
        self.rocket2.image.center_y = SCREEN_HEIGHT // 2

        # Initialize moving circle
        self.circle = MovingCircle(20)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.rocket1.draw()
        self.rocket2.draw()
        self.circle.draw()

    def on_update(self, delta_time):
        self.rocket1.update()
        self.rocket2.update()
        self.circle.update()

        # Update rocket with keyboard
        if self.key_list:
            self.rocket1.update_with_keyboard(self.key_list)

    def on_key_press(self, symbol, modifiers):
        if self.key_list is None:
            self.key_list = {}
        self.key_list[symbol] = True

    def on_key_release(self, symbol, modifiers):
        if self.key_list is not None and symbol in self.key_list:
            self.key_list[symbol] = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.rocket2.update_with_mouse(x, y)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Rocket Control")
    arcade.run()

if __name__ == "__main__":
    main()
