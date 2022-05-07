import pygame
import random
import sys
import os
import time
from pygame.locals import *

screen_width = 800
screen_height = 600
txt_c = (255, 255, 0)
bckg_c = (0, 0, 0)
FPS = 40
minimum_size_car = 10
maximum_size_car = 40
minimum_speed_car = 8
maximum_speed_car = 8
new_rate_car_added = 6
pl_movement_rate = 5
counting_seconds = 3


def Exit():
    pygame.quit()
    sys.exit()


def Press_Key_shortcut(): # waiting for player to press any key
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                Exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # escape quits
                    Exit()
                return


def player_crash(pl_crashRect, opponent):
    for ado in opponent:
        if pl_crashRect.colliderect(ado['rect']):
            return True
    return False


def txt_objects(t, f, s, x, y):
    txt_objects = f.render(t, 1, txt_c)
    txt_Rect = txt_objects.get_rect()
    txt_Rect.topleft = (x, y)
    s.blit(txt_objects, txt_Rect)


# set up pygame, the window, and the mouse cursor
pygame.init()
time_clock = pygame.time.Clock()
screen_display_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

# fonts
fontsize = pygame.font.SysFont(None, 30)

# sounds
game_over_music = pygame.mixer.Sound('audio_sound/crash.wav')
pygame.mixer.music.load('audio_sound/car.wav')
chuckle = pygame.mixer.Sound('audio_sound/chuckle.wav')

# images
player_car_photo = pygame.image.load('image/computer_car1.png')
computer_car3 = pygame.image.load('image/computer_car3.png')
computer_car4 = pygame.image.load('image/computer_car4.png')
gamer_Rect = player_car_photo.get_rect()
computer_car_photo = pygame.image.load('image/computer_car2.png')
another = [computer_car3, computer_car4, computer_car_photo]
w_left = pygame.image.load('image/left_side.png')
w_right = pygame.image.load('image/right_side.png')

# "welcome" screen
txt_objects('PRESS ANY KEY TO START THE GAME.', fontsize, screen_display_window, (screen_width / 3) - 30, (screen_height / 3))
txt_objects('GOOD LUCK AND ENJOY THE RACING', fontsize, screen_display_window, (screen_width / 3), (screen_height / 3) + 30)
pygame.display.update()
Press_Key_shortcut()
zero = 0
if not os.path.exists("datafiles/save.dat"):
    ado = open("datafiles/save.dat", 'w')
    ado.write(str(zero))
    ado.close()
datafile = open("datafiles/save.dat", 'r')
highest_scores = int(datafile.readline())
datafile.close()
while (counting_seconds > 0):
    # start of the game
    opponent = []
    score = 0
    gamer_Rect.topleft = (screen_width / 2, screen_height - 50)
    moving_left = moving_right = moving_up = moving_down = False
    counter_reverse = slowing_reverse = False
    adding_counter_opponent = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:  # the game loop
        score += 1  # increase score

        for event in pygame.event.get():

            if event.type == QUIT:
                Exit()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    counter_reverse = True
                if event.key == ord('x'):
                    slowing_reverse = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moving_right = False
                    moving_left = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moving_left = False
                    moving_right = True
                if event.key == K_UP or event.key == ord('w'):
                    moving_down = False
                    moving_up = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moving_up = False
                    moving_down = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    counter_reverse = False
                    score = 0
                if event.key == ord('x'):
                    slowing_reverse = False
                    score = 0
                if event.key == K_ESCAPE:
                    Exit()

                if event.key == K_LEFT or event.key == ord('a'):
                    moving_left = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moving_right = False
                if event.key == K_UP or event.key == ord('w'):
                    moving_up = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moving_down = False

        # Add new car at the top of the screen
        if not counter_reverse and not slowing_reverse:
            adding_counter_opponent += 1
        if adding_counter_opponent == new_rate_car_added:
            adding_counter_opponent = 0
            computer_car_size = 30
            new_computer_car = {'rect': pygame.Rect(random.randint(140, 485), 0 - computer_car_size, 23, 47),
                         'speed': random.randint(minimum_speed_car, maximum_speed_car),
                         'surface': pygame.transform.scale(random.choice(another), (23, 47)),
                                }
            opponent.append(new_computer_car)
            left_side = {'rect': pygame.Rect(0, 0, 126, 600),
                        'speed': random.randint(minimum_speed_car, maximum_speed_car),
                        'surface': pygame.transform.scale(w_left, (126, 599)),
                         }
            opponent.append(left_side)
            right_side = {'rect': pygame.Rect(497, 0, 303, 600),
                         'speed': random.randint(minimum_speed_car, maximum_speed_car),
                         'surface': pygame.transform.scale(w_right, (303, 599)),
                          }
            opponent.append(right_side)

        # Move the player around.
        if moving_left and gamer_Rect.left > 0:
            gamer_Rect.move_ip(-1 * pl_movement_rate, 0)
        if moving_right and gamer_Rect.right < screen_width:
            gamer_Rect.move_ip(pl_movement_rate, 0)
        if moving_up and gamer_Rect.top > 0:
            gamer_Rect.move_ip(0, -1 * pl_movement_rate)
        if moving_down and gamer_Rect.bottom < screen_height:
            gamer_Rect.move_ip(0, pl_movement_rate)

        for car in opponent:
            if not counter_reverse and not slowing_reverse:
                car['rect'].move_ip(0, car['speed'])
            elif counter_reverse:
                car['rect'].move_ip(0, -5)
            elif slowing_reverse:
                car['rect'].move_ip(0, 1)

        for car in opponent[:]:
            if car['rect'].top > screen_height:
                opponent.remove(car)

        # Draw the game world on the window.
        screen_display_window.fill(bckg_c)

        # Draw the score and top score.
        txt_objects('SCORE: %s' % (score), fontsize, screen_display_window, 128, 0)
        txt_objects('TOP SCORE: %s' % (highest_scores), fontsize, screen_display_window, 128, 20)
        txt_objects('REST LIFE: %s' % (counting_seconds), fontsize, screen_display_window, 128, 40)

        screen_display_window.blit(player_car_photo, gamer_Rect)

        for car in opponent:
            screen_display_window.blit(car['surface'], car['rect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if player_crash(gamer_Rect, opponent):
            if score > highest_scores:
                g = open("datafiles/save.dat", 'w')
                g.write(str(score))
                g.close()
                highest_scores = score
            break

        time_clock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    counting_seconds = counting_seconds - 1
    game_over_music.play()
    time.sleep(1)
    if (counting_seconds == 0):
        chuckle.play()
        txt_objects('GAME OVER', fontsize, screen_display_window, (screen_width / 3), (screen_height / 3))
        txt_objects('PRESS ANY KEY TO PLAY AGAIN.', fontsize, screen_display_window, (screen_width / 3) - 80, (screen_height / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        Press_Key_shortcut()
        counting_seconds = 3
        game_over_music.stop()
