import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOUR_CHANGE_EVENT=pygame.USEREVENT+2

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
GOLD=(255, 215, 0)
CHARTREUSE=(127, 255, 0)
# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width ):
      super().__init__()
      #create the sprit's surface  with dimentions & colour
      self.image=pygame.Surface([width, height])
      self.image.fill(colour)
      #get the sprite's rect to define position and size
      self.rect=self.image.get_rect()
      #set initial velocity
      self.velocity=[random.choice([-1, 1]), random.choice([-1, 1])]
      #[1, 1], [1, -1], [-1, 1], [-1, -1]<-(x, y)

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        #check for collisions with the left or right window edge
        if self.rect.left<=0 or self.rect.right>=500:
           boundary_hit=True
           self.velocity[0]=-self.velocity[0]
        #check for collisions with the top or bottom  window edge
        if self.rect.top<=0 or self.rect.bottom>=400:
           boundary_hit= True
           self.velocity[1]=-self.velocity[1]

        if boundary_hit==True:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))

    def change_colour(self):
        self.image.fill(random.choice([GOLD, MAGENTA, CHARTREUSE, WHITE]))

    

# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


all_sprites=pygame.sprite.Group()
#Create an odject from the sprite class
my_sprite=Sprite(WHITE, 40, 40)
#randomly positions the sprite
my_sprite.rect.x=random.randint(0, 450)
my_sprite.rect.y=random.randint(0, 350)
all_sprites.add(my_sprite)


# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Boundary Sprite")
# Set the initial background color
bg_color = BLUE
# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
       my_sprite.change_colour()
    # If the background color change event is triggered, change the background color
    elif event.type==BACKGROUND_COLOUR_CHANGE_EVENT:
       change_background_color()

  # Update all sprites
  all_sprites.update()

    # Fill the screen with the current background color
  screen.fill(bg_color)

  # Draw all sprites to the screen
  all_sprites.draw(screen)

  # Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()