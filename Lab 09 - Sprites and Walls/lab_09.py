import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_FLY = 0.5

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

NUMBER_OF_FLIES = 50

VIEWPORT_MARGIN = 220

CAMERA_SPEED = 0.1

PLAYER_MOVEMENT_SPEED = 7

SCORE_FONT_SIZE = 16
SCORE_COLOR = arcade.color.WHITE


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        self.player_list = None
        self.wall_list = None
        self.fly_list = None

        self.player_sprite = None
        self.score = 0

        self.fly_sound = arcade.load_sound(":resources:sounds/jump3.wav")

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_sprites = arcade.Camera()
        self.camera_gui = arcade.Camera()

        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(":resources:images/enemies/frog.png",
                                           scale=0.55)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        wallImage = ":resources:images/tiles/grassMid.png"
        verticalWall = ":resources:images/tiles/stoneCenter.png"

        for x in range(100, 550, 34):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range(300, 700, 64):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        for x in range(250, 730, 64):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        for x in range(417, 830, 64):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        for x in range(0, 195, 64):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        for x in range(0, 320, 64):
            wall = arcade.Sprite(wallImage, SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        for y in range(390, 700, 64):
            wall = arcade.Sprite(verticalWall, SPRITE_SCALING_BOX)
            wall.center_x = 900
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(830, 950, 60):
            wall = arcade.Sprite(verticalWall, SPRITE_SCALING_BOX)
            wall.center_x = 150
            wall.center_y = y
            self.wall_list.append(wall)

        max_x = 1000
        max_y = 1000

        for i in range(NUMBER_OF_FLIES):

            fly = arcade.Sprite(":resources:images/enemies/fly.png", SPRITE_SCALING_FLY)

            fly_placed_successfully = False

            while not fly_placed_successfully:
                fly.center_x = random.randrange(max_x)
                fly.center_y = random.randrange(max_y)

                wall_hit_list = arcade.check_for_collision_with_list(fly, self.wall_list)
                fly_hit_list = arcade.check_for_collision_with_list(fly, self.fly_list)

                if len(wall_hit_list) == 0 and len(fly_hit_list) == 0:
                    fly_placed_successfully = True

            self.fly_list.append(fly)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Render the screen. """

        self.clear()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.fly_list.draw()
        self.player_list.draw()

        screen_center_world = Vec2(
            self.camera_sprites.position[0] + self.width/2,
            self.camera_sprites.position[1] + self.height/2
        )

        score_offset = Vec2(-400, -290)

        score_position_world = screen_center_world + score_offset

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, score_position_world.x, score_position_world.y, SCORE_COLOR, SCORE_FONT_SIZE)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        self.physics_engine.update()

        self.apply_boundary_checks()

        self.scroll_to_player()

        if not self.game_over:
            self.fly_list.update()

            fly_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fly_list)

            for fly in fly_hit_list:
                fly.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.fly_sound)

            if len(self.fly_list) == 0:
                print("Game Over! Score:", self.score)
                self.game_over = True

    def apply_boundary_checks(self):
        """ Check boundaries and prevent character from going off screen """
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > 1000:
            self.player_sprite.right = 1000

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > 1000:
            self.player_sprite.top = 1000

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        """

        desired_x = self.player_sprite.center_x - self.width / 2
        desired_y = self.player_sprite.center_y - self.height / 2

        left_boundary = 0
        right_boundary = 1000
        top_boundary = 1000
        bottom_boundary = 0

        max_x = right_boundary - self.width
        max_y = top_boundary - self.height

        desired_x = max(left_boundary, min(desired_x, max_x))
        desired_y = max(bottom_boundary, min(desired_y, max_y))

        position = Vec2(desired_x, desired_y)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
