import pygame
from sys import exit
import random
import time

pygame.init()

config = {
    "screen_width": 800,
    "screen_height": 600,
    "pipe_space": 200,
    "pipe_gap_padding": 200,
    "pipe_scale": 0.2
}

screen = pygame.display.set_mode((config["screen_width"], config["screen_height"]))
pygame.display.set_caption("NotFlappyBird")
clock = pygame.time.Clock()

background = pygame.image.load("Assets/bg.png").convert_alpha()

text_font = pygame.font.Font(None, 30)
start_game_text_surf = text_font.render("Press Space To Start", False, "Red")
start_game_text_rect = start_game_text_surf.get_rect(center=(config["screen_width"] / 2, (config["screen_height"] / 2) - 25))

end_game_text_surf = text_font.render("Game Over!! Press Space to Start Again", False, "Red")
end_game_text_rect = end_game_text_surf.get_rect(center=(config["screen_width"] / 2, (config["screen_height"] / 2) - 25))

bird_surf = pygame.transform.scale_by(pygame.image.load("Assets/bird.png"), 0.075).convert_alpha()
bird_rect = bird_surf.get_rect(center=(100, (config["screen_height"] / 2) - 25))

score = 0
high_score = 0

class pipeSet:
    def __init__(self):
        self.out = False
        self.pipe_coordinates = self.get_rand_coor()
        self.top_surf = pygame.transform.scale_by(pygame.image.load("Assets/pipet.png"), config["pipe_scale"]).convert_alpha()
        self.top_rect = self.top_surf.get_rect(midbottom=self.pipe_coordinates["top"])

        self.bottom_surf = pygame.transform.scale_by(pygame.image.load("Assets/pipeb.png"), config["pipe_scale"]).convert_alpha()
        self.bottom_rect = self.bottom_surf.get_rect(midtop=self.pipe_coordinates["bottom"])

    def get_rand_coor(self):
        random.seed(time.time())
        mid_point = random.randint(config["pipe_gap_padding"] / 10, (config["screen_height"] - config["pipe_gap_padding"]) / 10) * 10
        return {
            "top": self.get_rand_coor_top(mid_point),
            "bottom": self.get_rand_coor_bottom(mid_point)
        }

    def get_rand_coor_top(self, mid_point):
        y_coor = mid_point - (config["pipe_space"] / 2)
        return config["screen_width"] + 300, y_coor

    def get_rand_coor_bottom(self, mid_point):
        y_coor = mid_point + (config["pipe_space"] / 2)
        return config["screen_width"] + 300, y_coor

    def is_out(self):
        return self.top_rect.bottomright[0] <= 0 and self.bottom_rect.bottomright[0] <= 0

    def get_pipe_rect(self):
        return [self.top_rect, self.bottom_rect]

    def is_collided_with(self, rect):
        return self.top_rect.colliderect(rect) or self.bottom_rect.colliderect(rect)


pipe_q = []

bird_y_pos = 50
bird_rot = 0

game_start = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            screen.blit(background, (0, 0))
            game_start = True
    if game_start:
        for i in range(0, 50):
            bird_rect.centerx += 3
            screen.blit(background, (0, 0))
            screen.blit(bird_surf, bird_rect)
            pygame.display.update()
            clock.tick(60)
        break
    screen.blit(background, (0, 0))
    screen.blit(start_game_text_surf, start_game_text_rect)
    screen.blit(bird_surf, bird_rect)

    pygame.display.update()
    clock.tick(60)

CREATEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CREATEEVENT, 1000)

def did_collide(pipe_q, bird_rect):
    for pipe in pipe_q:
        if bird_rect.colliderect(pipe.top_rect) or bird_rect.colliderect(pipe.bottom_rect):
            return True
    if bird_rect.centery > config["screen_height"] or bird_rect.centery < 0:
        return True
    return False

gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == CREATEEVENT:
            pipe_q.append(pipeSet())
            if pipe_q[0].out:
                pipe_q.pop()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        gravity = 0
        if bird_rot < 25:
            bird_rot += 20
        bird_rect.centery -= 10
    else:
        bird_rect.centery += gravity / 7
    gravity += 1.5
    screen.blit(background, (0, 0))
    screen.blit(pygame.transform.rotate(bird_surf, bird_rot), bird_rect)
    if bird_rot > -20:
        bird_rot -= 1

    exited_index = -1
    for pipe_num in range(len(pipe_q)):
        if pipe_q[pipe_num].top_rect.bottomright[0] <= 0:
            exited_index = pipe_num
        pipe_q[pipe_num].top_rect.centerx -= 10
        pipe_q[pipe_num].bottom_rect.centerx -= 10
        screen.blit(pipe_q[pipe_num].bottom_surf, pipe_q[pipe_num].bottom_rect)
        screen.blit(pipe_q[pipe_num].top_surf, pipe_q[pipe_num].top_rect)

        if pipe_q[pipe_num].top_rect.centerx == bird_rect.centerx:
            score += 1

    if exited_index != -1:
        pipe_q.pop(exited_index)

    if score > high_score:
        high_score = score

    score_surf = text_font.render(f"Score: {score}", False, "Black")
    high_score_surf = text_font.render(f"High Score: {high_score}", False, "Black")
    
    total_width = score_surf.get_width() + high_score_surf.get_width() + 20  
    screen.blit(score_surf, ((config["screen_width"] - total_width) / 2, 10))  
    screen.blit(high_score_surf, ((config["screen_width"] - total_width) / 2 + score_surf.get_width() + 20, 10))

    if did_collide(pipe_q, bird_rect):
        screen.blit(end_game_text_surf, end_game_text_rect)
        pygame.display.update()
        reset = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    pipe_q = []
                    bird_rect.centerx = 100
                    bird_rect.centery = (config["screen_height"] / 2) - 25
                    score = 0  
                    reset = True
            if reset:
                break
            clock.tick(60)

    pygame.display.update()
    clock.tick(60)
