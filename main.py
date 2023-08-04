import pygame, paddle

pygame.init()


screen_width = 800
screen_heighy = 800

squeare_size = 20

center_x = screen_width // 2
center_y = screen_heighy // 2

squeare_top_left_x = center_x - squeare_size // 2
squeare_top_left_y = center_y - squeare_size // 2

clock = pygame.time.Clock()

def get_delta_time():
    return clock.tick(120)


screen = pygame.display.set_mode((screen_width, screen_heighy))
pygame.display.set_caption("Pong")

paddle1 = paddle.Paddle(isAI = True, position = pygame.math.Vector2(20, 800), size=pygame.Vector2(20,120), speed=5)
paddle2 = paddle.Paddle(isAI = False, position = pygame.math.Vector2(1580, 800), size=pygame.Vector2(20,120), speed=5)

running = True

while running:
    
    keys_pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    paddle1.move(keys_pressed, get_delta_time())
    paddle2.move(keys_pressed, get_delta_time())
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1.get_rect())
    pygame.draw.rect(screen, (255, 255, 255), paddle2.get_rect())
    pygame.draw.rect(screen, (255,255, 255), (squeare_top_left_x, squeare_top_left_y, squeare_size, squeare_size))
    pygame.display.flip()

pygame.quit()



