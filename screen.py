import pygame
import consts
import game

pygame.init()
screen = pygame.display.set_mode((consts.WIDTH, consts.HIGHT))
pygame.display.set_caption("the BEST learning game")

screen.blit(consts.START_PICTURE, (0, 0))
pygame.display.flip()


# game intro screen
def intro():
    """
    print the intro screen' and the buttons.
    done. no need to touch
    :return: //
    """
    game_intro = True
    game_play = False
    # closing if needed
    while game_intro:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if consts.WIDTH / 2 -140 <= mouse[0] <= consts.WIDTH / 2 +140 and consts.HIGHT / 2 <= mouse[
                    1] <= consts.HIGHT / 2 + 40:
                    game_play = True
                    start_game()

        mouse = pygame.mouse.get_pos()
        if not game_play:
            if consts.WIDTH / 2 - 140 <= mouse[0] <= consts.WIDTH / 2 + 140 and consts.HIGHT / 2 <= mouse[
                1] <= consts.HIGHT / 2 + 40:
                pygame.draw.rect(screen, consts.BUTTON_PRESS, [consts.WIDTH / 2 -140, consts.HIGHT / 2, 280, 40])
            else:
                pygame.draw.rect(screen, consts.BUTTON_UNPRESSED, [consts.WIDTH / 2  -140, consts.HIGHT / 2, 280, 40])
            screen.blit(consts.BUTTON_TXT, (consts.WIDTH / 2-25 , consts.HIGHT / 2+10))

        pygame.display.flip()


def start_game():
    """
    creates the playing area screen.
    then sents to the game loop in game
    :return: //
    """
    screen.blit(consts.GAME_PICTURE, (0, 0))
    pygame.display.update()
    game.game_loop()


def add_poki(pokimon_list):
    """
    adds the pokimon to the screen
    :param pokimon_list:
    :return: //
    """
    screen.blit(pokimon_list[1], pokimon_list[0])
    print(pokimon_list[0])
    pygame.display.update()