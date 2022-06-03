import pygame
import time
import random

pygame.init()

White = (255,255,255)
red = (255, 0, 0)
black = (0, 0, 0)
display_width = 600
display_height = 400
gameWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SNAKE GAME")
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(0, display_width)
food_y = random.randint(0, display_height)
score = 0
snake_size = 20
snake_list = []
fps = 30
clock = pygame.time.Clock()
font =pygame.font.SysFont(None, 55)
def screen_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    print(snake_list)
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
snake_list = []
snake_lenght = 1

while not exit_game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -5
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0

            
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score += 1
        snake_lenght += 1
        food_x = random.randint(20, display_width /2)
        food_y = random.randint(20, display_height/2)
        
    gameWindow.fill(White)
    screen_text("score: " + str(score*10), red, 5, 5)
    pygame.draw.rect(gameWindow, red , [food_x, food_y, snake_size,snake_size])
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list)>snake_lenght:
        del snake_list[0]
    plot_snake(gameWindow, black , snake_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()