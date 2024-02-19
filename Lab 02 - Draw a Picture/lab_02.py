<<<<<<< HEAD


# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(800, 800, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.BRANDEIS_BLUE)
# Get ready to draw
arcade.start_render()
# (The drawing code will go here.)

# Draw a rectangle
# Left of 0, right of 799
# Top of 350, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 799, 350, 0, arcade.color.DARK_PASTEL_GREEN)
# Draw a sun
arcade.draw_circle_filled(150, 700, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(50, 700, 150, 700, arcade.color.YELLOW, 3)
arcade.draw_line(190, 700, 250, 700, arcade.color.YELLOW, 3)
arcade.draw_line(150, 720, 150, 790, arcade.color.YELLOW, 3)
arcade.draw_line(150, 700, 150, 600, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(150, 700, 225, 760, arcade.color.YELLOW, 3)
arcade.draw_line(150, 700, 75, 760, arcade.color.YELLOW, 3)
arcade.draw_line(225, 640, 150, 700, arcade.color.YELLOW, 3)
arcade.draw_line(75, 640, 150, 700, arcade.color.YELLOW, 3)

# Draw the cloud
arcade.draw_circle_filled(650, 700, 40, arcade.color.WHITE)
arcade.draw_circle_filled(690, 700, 50, arcade.color.WHITE)
arcade.draw_circle_filled(730, 700, 40, arcade.color.WHITE)
arcade.draw_circle_filled(670, 670, 40, arcade.color.WHITE)
arcade.draw_circle_filled(710, 670, 40, arcade.color.WHITE)
# Draw another cloud
arcade.draw_circle_filled(400, 600, 50, arcade.color.WHITE)
arcade.draw_circle_filled(440, 600, 60, arcade.color.WHITE)
arcade.draw_circle_filled(480, 600, 50, arcade.color.WHITE)
arcade.draw_circle_filled(420, 570, 50, arcade.color.WHITE)
arcade.draw_circle_filled(460, 570, 50, arcade.color.WHITE)
# Draw the house body
arcade.draw_rectangle_filled(200, 100, 200, 100, arcade.color.CHOCOLATE)

# Draw the roof
arcade.draw_triangle_filled(200, 300, 50, 150, 350, 150, arcade.color.BRIGHT_MAROON)

# Draw the door
arcade.draw_rectangle_filled(200, 90, 40, 80, arcade.color.BLACK_OLIVE)

# Draw the window
arcade.draw_rectangle_filled(140, 100, 35, 40, arcade.color.CAPRI)
arcade.draw_rectangle_filled(260, 100, 35, 40, arcade.color.CAPRI)
# Tree trunk
# Center of 700, 100
# Width of 30
# Height of 90
arcade.draw_rectangle_filled(700, 100, 30, 90, arcade.csscolor.SIENNA)
# Tree top
arcade.draw_circle_filled(700, 210, 70, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (420, 130), (580, 130), (500, 220)
# (420, 160), (580, 160), (500, 250)
# (420, 190), (580, 190), (500, 300)
arcade.draw_rectangle_filled(500, 100, 30, 90, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(420, 130, 580, 130, 500, 220, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(420, 160, 580, 160, 500, 250, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(420, 190, 580, 190, 500, 300, arcade.csscolor.DARK_GREEN)

# Mountain
# Triangle is made of these three points:
# (0,350), (500,350), (250,500)
arcade.draw_triangle_filled(0, 350, 500, 350, 250, 500, arcade.color.BRONZE)
# Snow top of mountain
# Triangle is made of these three points:
# (250,500), (167,450), (333,450)
arcade.draw_triangle_filled(250, 500, 167, 450, 333, 450, arcade.color.WHITE)
# Another Mountain
arcade.draw_triangle_filled(350, 350, 850, 350, 600, 500, arcade.color.BRONZE)
arcade.draw_triangle_filled(600, 500, 517, 450, 683, 450, arcade.color.WHITE)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
=======


# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(800, 800, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.BRANDEIS_BLUE)
# Get ready to draw
arcade.start_render()
# (The drawing code will go here.)

# Draw a rectangle
# Left of 0, right of 799
# Top of 350, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 799, 350, 0, arcade.color.DARK_PASTEL_GREEN)
# Draw a sun
arcade.draw_circle_filled(150, 700, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(50, 700, 150, 700, arcade.color.YELLOW, 3)
arcade.draw_line(190, 700, 250, 700, arcade.color.YELLOW, 3)
arcade.draw_line(150, 720, 150, 790, arcade.color.YELLOW, 3)
arcade.draw_line(150, 700, 150, 600, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(150, 700, 225, 760, arcade.color.YELLOW, 3)
arcade.draw_line(150, 700, 75, 760, arcade.color.YELLOW, 3)
arcade.draw_line(225, 640, 150, 700, arcade.color.YELLOW, 3)
arcade.draw_line(75, 640, 150, 700, arcade.color.YELLOW, 3)

# Draw the cloud
arcade.draw_circle_filled(650, 700, 40, arcade.color.WHITE)
arcade.draw_circle_filled(690, 700, 50, arcade.color.WHITE)
arcade.draw_circle_filled(730, 700, 40, arcade.color.WHITE)
arcade.draw_circle_filled(670, 670, 40, arcade.color.WHITE)
arcade.draw_circle_filled(710, 670, 40, arcade.color.WHITE)
# Draw another cloud
arcade.draw_circle_filled(400, 600, 50, arcade.color.WHITE)
arcade.draw_circle_filled(440, 600, 60, arcade.color.WHITE)
arcade.draw_circle_filled(480, 600, 50, arcade.color.WHITE)
arcade.draw_circle_filled(420, 570, 50, arcade.color.WHITE)
arcade.draw_circle_filled(460, 570, 50, arcade.color.WHITE)
# Draw the house body
arcade.draw_rectangle_filled(200, 100, 200, 100, arcade.color.CHOCOLATE)

# Draw the roof
arcade.draw_triangle_filled(200, 300, 50, 150, 350, 150, arcade.color.BRIGHT_MAROON)

# Draw the door
arcade.draw_rectangle_filled(200, 90, 40, 80, arcade.color.BLACK_OLIVE)

# Draw the window
arcade.draw_rectangle_filled(140, 100, 35, 40, arcade.color.CAPRI)
arcade.draw_rectangle_filled(260, 100, 35, 40, arcade.color.CAPRI)
# Tree trunk
# Center of 700, 100
# Width of 30
# Height of 90
arcade.draw_rectangle_filled(700, 100, 30, 90, arcade.csscolor.SIENNA)
# Tree top
arcade.draw_circle_filled(700, 210, 70, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (420, 130), (580, 130), (500, 220)
# (420, 160), (580, 160), (500, 250)
# (420, 190), (580, 190), (500, 300)
arcade.draw_rectangle_filled(500, 100, 30, 90, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(420, 130, 580, 130, 500, 220, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(420, 160, 580, 160, 500, 250, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(420, 190, 580, 190, 500, 300, arcade.csscolor.DARK_GREEN)

# Mountain
# Triangle is made of these three points:
# (0,350), (500,350), (250,500)
arcade.draw_triangle_filled(0, 350, 500, 350, 250, 500, arcade.color.BRONZE)
# Snow top of mountain
# Triangle is made of these three points:
# (250,500), (167,450), (333,450)
arcade.draw_triangle_filled(250, 500, 167, 450, 333, 450, arcade.color.WHITE)
# Another Mountain
arcade.draw_triangle_filled(350, 350, 850, 350, 600, 500, arcade.color.BRONZE)
arcade.draw_triangle_filled(600, 500, 517, 450, 683, 450, arcade.color.WHITE)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
>>>>>>> a76c444c75b7123aa4c17b28fa90d412bb0f4c33
