import arcade

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 799, 350, 0, arcade.color.DARK_PASTEL_GREEN)

def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 40, y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 80, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y - 30, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 60, y - 30, 40, arcade.color.WHITE)

def draw_house():
    arcade.draw_rectangle_filled(200, 100, 200, 100, arcade.color.CHOCOLATE)
    arcade.draw_triangle_filled(200, 300, 50, 150, 350, 150, arcade.color.BRIGHT_MAROON)
    arcade.draw_rectangle_filled(200, 90, 40, 80, arcade.color.BLACK_OLIVE)
    arcade.draw_rectangle_filled(140, 100, 35, 40, arcade.color.CAPRI)
    arcade.draw_rectangle_filled(260, 100, 35, 40, arcade.color.CAPRI)

def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 30, 90, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x, y + 110, 70, arcade.csscolor.DARK_GREEN)

def draw_mountain(x1, y1, x2, y2, x3, y3):
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.BRONZE)

def draw_bird(x, y):
    arcade.draw_line(x, y, x + 20, y + 10, arcade.color.BLACK, 2)
    arcade.draw_line(x, y, x + 20, y - 10, arcade.color.BLACK, 2)

def main():
    arcade.open_window(800, 800, "Drawing Example")
    arcade.set_background_color(arcade.color.BRANDEIS_BLUE)
    arcade.start_render()

    draw_grass()
    draw_cloud(650, 700)
    draw_cloud(500, 600)
    draw_cloud(320, 700)
    draw_cloud(120, 700)
    draw_house()
    draw_tree(730, 100)
    draw_tree(570, 100)
    draw_tree(420, 100)
    draw_mountain(0, 350, 500, 350, 250, 500)
    draw_mountain(350, 350, 850, 350, 600, 500)

    # Draw a bird flying in the sky
    draw_bird(400, 550)
    draw_bird(400, 580)
    draw_bird(400, 520)
    draw_bird(350, 565)
    draw_bird(350, 535)
    draw_bird(300, 550)

    draw_bird(150, 550)
    draw_bird(150, 580)
    draw_bird(150, 520)
    draw_bird(100, 565)
    draw_bird(100, 535)
    draw_bird(50, 550)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
