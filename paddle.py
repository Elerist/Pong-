from typing import Any
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, isAI: bool, position: pygame.Vector2, size: pygame.Vector2, speed: float):
        self.position = position 
        self.size =  size 
        self.isAI = isAI
        self.speed = speed
    
    def get_rect(self):
        center_x = self.position.x // 2
        center_y = self.position.y // 2
        square_top_left_x = center_x - self.size.x // 2
        square_top_left_y = center_y - self.size.y // 2
        
        #print("center_y: ", center_y, "center_x: ", center_x)
        #print("square_top_left_x: ", square_top_left_x, "square_top_left_y: ", square_top_left_y) 
        
        return pygame.Rect(square_top_left_x, square_top_left_y, self.size.x, self.size.y)


    def move(self, keys_pressed, deltatime):
        if self.isAI:
            pass
        else:
            self.adjust_by_player(keys_pressed, deltatime)

    def adjust_by_player(self, keys_pressed, deltatime):
        if keys_pressed[pygame.K_UP]:
            self.position.y -= self.speed * deltatime
        if keys_pressed[pygame.K_DOWN]:
            self.position.y += self.speed * deltatime
        
        



