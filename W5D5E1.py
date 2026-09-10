import pygame
import time 
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
over_font = pygame.font.Font(None, 60)
game_state = "start"

player_x, player_y = 270, 350
vel = 5
player_speed = 5
start_time = time.time()
elapsed_time = 0

# star
star_x = random.randint(0, 560)
star_y = 0
star_speed = 2
score = 0
misses = 0

running = True
while running:
    clock.tick(60)
    elapsed_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                game_state = "playing"

            elif game_state == "game_over" and event.key == pygame.K_SPACE:
                score = 0
                misses = 0
                star_y = 0
                star_x = random.randint(0, 560)
                player_x = 270
                star_speed = 2
                start_time = time.time()
                game_state = "playing"

    screen.fill((20, 20, 40))

    if game_state == "start":
        start_text = font.render("Press SPACEBAR to Start Game", True, (255, 255, 255))
        screen.blit(start_text, (130, 180))

    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= vel
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < 500:
            player_x += vel
            player_x += player_speed

        player_rect = pygame.Rect(player_x, player_y, 100, 20)
        star_rect = pygame.Rect(star_x, star_y, 20, 20)
        star_y += star_speed
        star_y += 3

        if star_y > 400:
            star_y = 0
            star_x = random.randint(0, 560)
            misses += 1

        if player_rect.colliderect(star_rect):
            score += 1
            star_y = 0
            star_x = random.randint(0, 560)
            star_speed += 0.5

        if misses >= 3:
            game_state = "game_over"

        pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, 100, 20))
        pygame.draw.circle(screen, (255, 255, 0), (star_x, star_y), 10)

        timer_text = font.render(f"Time: {elapsed_time:.1f}s", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 50))

        misses_text = font.render(f"Misses: {misses}", True, (255, 255, 255))
        screen.blit(misses_text, (10, 90))

    elif game_state == "game_over":
        over_text = over_font.render("Game Over", True, (255, 255, 255))
        screen.blit(over_text, (200, 120))

        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(final_score_text, (200, 180))

        retry_text = font.render("Press SPACEBAR to Play Again", True, (255, 255, 255))
        screen.blit(retry_text, (200, 240))

    pygame.display.flip()

pygame.quit()