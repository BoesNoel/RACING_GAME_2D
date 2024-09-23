import pygame
# Initialize Pygame

def move_player(vel_x, vel_y):
    player[0] += vel_x
    player[1] += vel_y

# TODO make it so that player can move to very edge of wall -> move(min{dist, vel})
#def player_in_bounds(player :list, street :list, width : int):
    


pygame.init()
width, height = 800, 600
screen: pygame.Surface = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
STREET_COLOR = (143,143,142)
GRASS_COLOR = (29,74,23)

# Player position
player = [381, 461, 10, 10]
vel = 3
#
street = [100, 100, 600, 400]
street_width = 60

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player[0] > street[0] + vel:
        move_player(-vel, 0)

    if keys[pygame.K_RIGHT] and player[0] < street[0] + street[2] - player[2] - vel:
        move_player(vel, 0)

    if keys[pygame.K_UP] and player[1] > street[1] + vel:
        move_player(0, -vel)

    if keys[pygame.K_DOWN] and player[1] < street[1] + street[3] - player[3] - vel:
        move_player(0, vel)


    # Clear the screen
    screen.fill(GRASS_COLOR)
    # Draw racing street
    pygame.draw.rect(screen, STREET_COLOR, pygame.Rect(street))
    # Draw grass in the middle
    pygame.draw.rect(screen, GRASS_COLOR, pygame.Rect(street[0] + street_width, street[1] + street_width, 600-2*street_width, 400-2*street_width))
    # Draw player (red)
    pygame.draw.rect(screen, RED, pygame.Rect(player))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
