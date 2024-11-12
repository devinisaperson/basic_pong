# import needed libraries
import pygame
import random

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# paddle CONSTANTS and variables
PADDLE_COLOR = pygame.Color(255,255,255,255)
PADDLE_SPEED = 10
paddle_rect = pygame.Rect(120,40,20,100)

# ball CONSTANTS and variables
BALL_COLOR = pygame.Color(255,255,255,255)
ball_velocity = [8,8]
ball_rect = pygame.Rect(200,random.randrange(100,screen_height-100),10,10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # UPDATING THE GAMESTATE
    # move paddle according to player input
    if pygame.key.get_pressed()[pygame.K_UP]:
        paddle_rect.move_ip(0,-PADDLE_SPEED)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        paddle_rect.move_ip(0,PADDLE_SPEED)
    
    #if paddle is out of bounds, move it in bounds
    if paddle_rect.top < 0:
        paddle_rect.top = 0
    elif paddle_rect.bottom > screen_height:
        paddle_rect.bottom = screen_height

    ball_rect.move_ip(ball_velocity[0],ball_velocity[1])

    #if ball is out of bounds, move it in bounds
    if ball_rect.top < 0:
        ball_rect.top = 0

        # change its velocity to make it bounce
        # otherwise it gets stuck!
        ball_velocity[1] = abs(ball_velocity[1])
    elif ball_rect.bottom > screen_height:
        ball_rect.bottom = screen_height
        ball_velocity[1] = -abs(ball_velocity[1])
    
    if ball_rect.right > screen_width:
        ball_rect.right = screen_width
        ball_velocity[0] = -abs(ball_velocity[0])
    elif ball_rect.left < 0:
        # if it has moved left of the screen, you lose!
        running = False
    
    # check for a collision between the ball and the paddle
    if ball_rect.colliderect(paddle_rect):
        #we want to "push" the ball out to the right of the paddle
        ball_rect.left = paddle_rect.right
        
        # change the velocity to make the ball bounce
        # room for a lot of fun stuff in this if statement!
        ball_velocity[0] = abs(ball_velocity[0]) + 2

    # RENDERING THE GAMESTATE
    pygame.draw.rect(screen, PADDLE_COLOR, paddle_rect)
    pygame.draw.rect(screen, BALL_COLOR, ball_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
