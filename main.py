# # Simple pygame program

# # Import and initialize the pygame library
# import pygame
# pygame.init()

# # Set up the drawing window
# screen = pygame.display.set_mode([500, 500])

# # Running the game until the user asks to quit
# running = True
# while running:

#     # creating an if statement for the close button
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Filling the background color with a gray
#     screen.fill((55, 55, 55))

#     # Drawing a solid purple circle in the center
#     pygame.draw.circle(screen, (0, 0, 251), (251, 251), 74)
#     # Flip the display
#     pygame.display.flip()

# # Done! Time to quit.
# pygame.quit()
import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
    # app.run(debug=True, host="0.0.0.0", port=5000)
