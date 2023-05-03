import pygame
from pygame.locals import *

width, height = 650, 650


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height), RESIZABLE)
    game(screen)


def init_players():
    red_player_image = pygame.image.load("resources/images/red.png")
    red_player_image = pygame.transform.scale(red_player_image, (width // 10, height // 50 * 8))

    purple_player_image = pygame.image.load("resources/images/purple.png")
    purple_player_image = pygame.transform.scale(purple_player_image, (width // 10, height // 50 * 8))

    orange_player_image = pygame.image.load("resources/images/orange.png")
    orange_player_image = pygame.transform.scale(orange_player_image, (width // 10, height // 50 * 8))

    green_player_image = pygame.image.load("resources/images/green.png")
    green_player_image = pygame.transform.scale(green_player_image, (width // 10, height // 50 * 8))

    yellow_player_image = pygame.image.load("resources/images/yellow.png")
    yellow_player_image = pygame.transform.scale(yellow_player_image, (width // 10, height // 50 * 8))

    blue_player_image = pygame.image.load("resources/images/blue.png")
    blue_player_image = pygame.transform.scale(blue_player_image, (width // 10, height // 50 * 8))

    board_image = pygame.image.load("resources/images/board.png")
    board_image = pygame.transform.scale(board_image, (width // 13 * 9, height // 13 * 9))

    players_images = [red_player_image, purple_player_image, orange_player_image, green_player_image,
                      yellow_player_image,
                      blue_player_image, board_image]

    return players_images


def init_levels():
    first_positions = [[0 for i in range(40)] for j in range(6)]

    # RED initial positions
    first_positions[0] = [[0, 4], [0, 0], [3, 0], [4, 2], [3, 0],
                          [3, 0], [1, 1], [1, 1], [2, 4], [0, 0],
                          [2, 3], [4, 4], [1, 1], [3, 0], [0, 0],
                          [3, 4], [3, 0], [2, 4], [0, 0], [4, 4],
                          [2, 4], [0, 0], [3, 0], [2, 3], [3, 0],
                          [2, 3], [3, 4], [2, 4], [2, 4], [2, 4],
                          [4, 4], [3, 0], [0, 0], [3, 4], [2, 4],
                          [2, 4], [0, 0], [3, 3], [3, 4], [3, 0]]

    # purple initial positions
    first_positions[1] = [[2, 1], [3, 2], [3, 2], [-1], [1, 3],
                          [1, 0], [-1], [3, 3], [3, 1], [4, 1],
                          [0, 3], [1, 4], [4, 1], [4, 2], [0, 2],
                          [4, 2], [3, 2], [0, 0], [1, 2], [2, 4],
                          [0, 2], [1, 1], [0, 4], [2, 4], [1, 3],
                          [2, 4], [0, 3], [0, 4], [4, 0], [4, 2],
                          [0, 3], [4, 0], [0, 3], [0, 3], [2, 3],
                          [4, 1], [0, 4], [0, 4], [3, 1], [0, 4]]

    # orange initial positions
    first_positions[2] = [[3, 4], [0, 4], [2, 4], [2, 4], [4, 4],
                          [1, 4], [-1], [4, 4], [0, 4], [3, 3],
                          [2, 4], [3, 4], [3, 4], [2, 4], [0, 4],
                          [0, 3], [2, 4], [4, 0], [3, 4], [3, 4],
                          [2, 3], [4, 3], [3, 4], [4, 4], [4, 3],
                          [4, 4], [-1], [4, 4], [4, 4], [4, 3],
                          [2, 4], [3, 4], [4, 4], [3, 3], [4, 4],
                          [4, 3], [4, 4], [4, 4], [0, 4], [4, 4]]

    # green initial positions
    first_positions[3] = [[-1], [2, 3], [0, 3], [2, 1], [0, 4],
                          [3, 3], [1, 0], [1, 4], [2, 2], [0, 2],
                          [4, 3], [1, 1], [1, 3], [0, 3], [3, 3],
                          [-1], [0, 4], [2, 0], [2, 3], [2, 0],
                          [2, 2], [0, 3], [-1], [3, 0], [2, 3],
                          [2, 0], [2, 1], [-1], [0, 4], [0, 3],
                          [2, 0], [0, 3], [3, 4], [2, 0], [0, 4],
                          [0, 3], [4, 0], [-1], [0, 1], [2, 4]]

    # yellow initial positions
    first_positions[4] = [[-1], [1, 1], [1, 1], [-1], [2, 1],
                          [-1], [1, 3], [4, 0], [1, 0], [2, 0],
                          [2, 2], [3, 3], [2, 0], [1, 1], [2, 1],
                          [0, 1], [1, 1], [-1], [4, 1], [1, 4],
                          [4, 1], [4, 0], [1, 3], [4, 2], [0, 0],
                          [1, 2], [4, 1], [3, 0], [0, 0], [3, 0],
                          [0, 1], [0, 2], [4, 1], [-1], [4, 0],
                          [0, 1], [1, 3], [2, 0], [-1], [0, 1]]

    # blue initial positions
    first_positions[5] = [[-1], [-1], [-1], [0, 2], [-1],
                          [-1], [4, 2], [-1], [-1], [-1],
                          [2, 1], [3, 1], [-1], [4, 0], [-1],
                          [4, 0], [-1], [-1], [2, 0], [4, 0],
                          [1, 0], [-1], [0, 0], [0, 2], [-1],
                          [4, 0], [3, 1], [1, 0], [-1], [1, 0],
                          [4, 0], [-1], [1, 0], [3, 1], [0, 0],
                          [2, 0], [3, 1], [0, 0], [2, 1], [-1]]

    for i in range(len(first_positions)):
        for j in range(len(first_positions[i])):
            for h in range(len(first_positions[i][j])):
                if len(first_positions[i][j]) > 1:
                    first_positions[i][j][h] = 4 - first_positions[i][j][h]

    return first_positions


def get_mouse_clicked_pos():
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    return pressed[0], pos[0], pos[1]


def use_events(events):
    for event in events:
        # if event.type == pygame.VIDEORESIZE:
        #     width, height = event.size
        #     if width > 700:
        #         small_screen = False
        #     else:
        #         small_screen = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


def optional_move(board):
    optional_moves = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                h = 1
                right = 0
                left = 0
                up = 0
                down = 0
                while h < 5:
                    if i + h <= 4:
                        if board[i + h][j] == 1:
                            if h > 1:
                                if right == 0:
                                    optional_moves.append([[i, j], 0, h - 1])
                                    right = 1
                            else:
                                right = -1
                    if i - h >= 0:
                        if board[i - h][j] == 1:
                            if h > 1:
                                if left == 0:
                                    optional_moves.append([[i, j], 0, -1 * (h - 1)])
                                    left = 1
                            else:
                                left = -1
                    if j + h <= 4:
                        if board[i][j + h] == 1:
                            if h > 1:
                                if up == 0:
                                    optional_moves.append([[i, j], 1, h - 1])
                                    up = 1
                            else:
                                up = -1
                    if j - h >= 0:
                        if board[i][j - h] == 1:
                            if h > 1:
                                if down == 0:
                                    optional_moves.append([[i, j], 1, -1 * (h - 1)])
                                    down = 1
                            else:
                                down = -1
                    h += 1
    return optional_moves


def touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves):
    if abs(y_mouse - (height // 12 + height // 40 + height // 12 * touched_pos[1] * 2)) <= height // 24 // 2:
        if x_mouse - (width // 12 * 2 + width // 12 * touched_pos[0] * 2) >= width // 12 - width // 24:
            for i in range(len(optional_moves)):
                if optional_moves[i][0] == touched_pos:
                    if optional_moves[i][1] == 0:
                        if optional_moves[i][2] > 0:
                            return optional_moves[i]
        if x_mouse - (width // 12 * 2 + width // 12 * touched_pos[0] * 2) <= -1 * (width // 12 - width // 24):
            for i in range(len(optional_moves)):
                if optional_moves[i][0] == touched_pos:
                    if optional_moves[i][1] == 0:
                        if optional_moves[i][2] < 0:
                            return optional_moves[i]

    if abs(x_mouse - (width // 12 + width // 12 + width // 12 * touched_pos[0] * 2)) <= width // 24 // 2:
        if y_mouse - (height // 40 + height // 12 + height // 12 * touched_pos[1] * 2) >= height // 12 - height // 24:
            for i in range(len(optional_moves)):
                if optional_moves[i][0] == touched_pos:
                    if optional_moves[i][1] == 1:
                        if optional_moves[i][2] > 0:
                            return optional_moves[i]
        if y_mouse - (height // 40 + height // 12 + height // 12 * touched_pos[1] * 2) <= -1 * (
                height // 12 - height // 24):
            for i in range(len(optional_moves)):
                if optional_moves[i][0] == touched_pos:
                    if optional_moves[i][1] == 1:
                        if optional_moves[i][2] < 0:
                            return optional_moves[i]
    return [10, 10], 0, 10


def first_instructions_screen(screen):
    instructions_1 = pygame.image.load("resources/images/instructions_1.png")
    instructions_1 = pygame.transform.scale(instructions_1, (width, height // 2))
    screen.blit(instructions_1, (0, 0))

    instructions_2 = pygame.image.load("resources/images/instructions_2.png")
    instructions_2 = pygame.transform.scale(instructions_2, (width, height // 2))
    screen.blit(instructions_2, (0, height // 2))


def draw_board(screen):
    # background
    for i in range(height // 12 * 10):
        pygame.draw.line(screen, [180, 180, 180], [width // 12, height // 40 + i], [width // 12 * 11, height // 40 + i])

    # red center
    for i in range(width // 12 * 5, width // 12 * 7):
        if abs(i - width // 12 * 6) > width // 12 // 3:
            pygame.draw.line(screen, [200, 50, 50], [i, height // 40 + height // 12 * 4],
                             [i, height // 40 + height // 12 * 6])
    for i in range(height // 12 * 4, height // 12 * 6):
        if abs(i - height // 12 * 5) > height // 12 // 3:
            pygame.draw.line(screen, [200, 50, 50], [width // 12 * 5, i + height // 40],
                             [width // 12 * 7, i + height // 40])

    for i in range(width // 12 * 5, width // 12 * 7):
        if abs(i - width // 12 * 6) <= width // 12 // 3 and i % (width // 12 // 3) == 0:
            for j in range(3):
                pygame.draw.line(screen, [150, 25, 25], [i - 1 + j, height // 40 + height // 12 * 4],
                                 [i - 1 + j, height // 40 + height // 12 * 4 + height // 12 // 3 * 2])
                pygame.draw.line(screen, [150, 25, 25],
                                 [i - 1 + j, height // 40 + height // 12 * 5 + height // 12 // 3],
                                 [i - 1 + j, height // 40 + height // 12 * 6])
    for i in range(height // 12 * 4, height // 12 * 6):
        if abs(i - height // 12 * 5) <= height // 12 // 3 and i % (height // 12 // 3) == 0:
            for j in range(3):
                pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5, height // 40 + i - 1 + j],
                                 [width // 12 * 5 + width // 12 // 3 * 2, height // 40 + i - 1 + j])
                pygame.draw.line(screen, [150, 25, 25],
                                 [width // 12 * 6 + width // 12 // 3 * 1, height // 40 + i - 1 + j],
                                 [width // 12 * 7, height // 40 + i - 1 + j])
    for j in range(3):
        pygame.draw.line(screen, [150, 25, 25],
                         [width // 12 * 6 + width // 12 // 3 * 1,
                          height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j],
                         [width // 12 * 7, height // 40 + height // 12 * 4 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25],
                         [width // 12 * 6 + width // 12 // 3 * 1,
                          height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j],
                         [width // 12 * 7, height // 40 + height // 12 * 6 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5, height // 40 + height // 12 * 4 - 1 + j],
                         [width // 12 * 5 + width // 12 // 3 * 2,
                          height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5, height // 40 + height // 12 * 6 - 1 + j],
                         [width // 12 * 5 + width // 12 // 3 * 2,
                          height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5 + width // 12 // 3 * 2,
                                                 height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j],
                         [width // 12 * 6 + height // 12 // 3,
                          height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5 + width // 12 // 3 * 2,
                                                 height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j],
                         [width // 12 * 6 + height // 12 // 3,
                          height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 5 + width // 12 // 3 * 2 - 1 + j,
                                                 height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j],
                         [width // 12 * 5 + width // 12 // 3 * 2 - 1 + j,
                          height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j])
        pygame.draw.line(screen, [150, 25, 25], [width // 12 * 6 + width // 12 // 3 - 1 + j,
                                                 height // 40 + height // 12 * 4 + height // 12 // 3 * 2 - 1 + j],
                         [width // 12 * 6 + width // 12 // 3 - 1 + j,
                          height // 40 + height // 12 * 5 + height // 12 // 3 - 1 + j])

    # frames
    for i in range(height // 12 * 11):
        if i % (height // 12 * 10 // 5) == 0:
            for j in range(5):
                pygame.draw.line(screen, [100, 100, 100], [width // 12, height // 40 + i - 2 + j],
                                 [width // 12 * 11, height // 40 + i - 2 + j])
    for i in range(width // 12 * 11):
        if i % (width // 12 * 10 // 5) == 0:
            for j in range(5):
                pygame.draw.line(screen, [100, 100, 100], [width // 12 + i - 2 + j, height // 40],
                                 [width // 12 + i - 2 + j, height // 40 + height // 12 * 10])


def second_instructions_screen(screen):
    instructions_3 = pygame.image.load("resources/images/instructions_3.png")
    instructions_3 = pygame.transform.scale(instructions_3, (width // 2, height // 8 * 7))
    screen.blit(instructions_3, (0, 0))

    instructions_4 = pygame.image.load("resources/images/instructions_4.png")
    instructions_4 = pygame.transform.scale(instructions_4, (width // 2, height // 8 * 7))
    screen.blit(instructions_4, (width // 2, 0))


def third_instructions_screen(screen):
    instructions_5 = pygame.image.load("resources/images/instructions_5.png")
    instructions_5 = pygame.transform.scale(instructions_5, (width // 2, height // 8 * 7))
    screen.blit(instructions_5, (0, 0))

    instructions_6 = pygame.image.load("resources/images/instructions_6.png")
    instructions_6 = pygame.transform.scale(instructions_6, (width // 2, height // 8 * 7))
    screen.blit(instructions_6, (width // 2, 0))


def starting_screen(screen, players_images):
    red_player_image = players_images[0]
    purple_player_image = players_images[1]
    orange_player_image = players_images[2]
    green_player_image = players_images[3]
    yellow_player_image = players_images[4]
    blue_player_image = players_images[5]
    board_image = players_images[-1]

    screen.blit(red_player_image, (width // 13.333 * 1, height // 4 * 3))
    screen.blit(purple_player_image, (width // 13.333 * 5, height // 4 * 3))
    screen.blit(orange_player_image, (width // 13.333 * 11, height // 4 * 3))
    screen.blit(green_player_image, (width // 13.333 * 9, height // 4 * 3))
    screen.blit(yellow_player_image, (width // 13.333 * 3, height // 4 * 3))
    screen.blit(blue_player_image, (width // 13.333 * 7, height // 4 * 3))
    screen.blit(board_image, (width // 6.6666, height // 40))

    play_image = pygame.image.load("resources/images/the_word_play.png")
    play_image = pygame.transform.scale(play_image, (width // 2, height // 4))
    screen.blit(play_image, (width // 13.5 * 3.4, height // 16))

    instructions_image = pygame.image.load("resources/images/the_word_instructions.png")
    instructions_image = pygame.transform.scale(instructions_image, (width // 2, height // 8))
    screen.blit(instructions_image, (width // 13.5 * 3.4, height // 16 * 7))


def choose_level_screen(screen, players_images):
    player8 = pygame.image.load("resources/images/levels.png")
    player8 = pygame.transform.scale(player8, (width, height // 8 * 5))
    screen.blit(player8, (0, 0))

    red_player_image = players_images[0]
    purple_player_image = players_images[1]
    orange_player_image = players_images[2]
    green_player_image = players_images[3]
    yellow_player_image = players_images[4]
    blue_player_image = players_images[5]

    screen.blit(red_player_image, (width // 13.333 * 1, height // 16 * 11))
    screen.blit(purple_player_image, (width // 13.333 * 5, height // 16 * 11))
    screen.blit(orange_player_image, (width // 13.333 * 11, height // 16 * 11))
    screen.blit(green_player_image, (width // 13.333 * 9, height // 16 * 11))
    screen.blit(yellow_player_image, (width // 13.333 * 3, height // 16 * 11))
    screen.blit(blue_player_image, (width // 13.333 * 7, height // 16 * 11))


def level_screen(screen, red_pos, purple_pos, orange_pos, green_pos, yellow_pos, blue_pos, players_images, moves_num,
                  deleted_moves_num, level):
    red_player_image = players_images[0]
    purple_player_image = players_images[1]
    orange_player_image = players_images[2]
    green_player_image = players_images[3]
    yellow_player_image = players_images[4]
    blue_player_image = players_images[5]

    draw_board(screen)
    center_x = (width / 12 * 2 - width / 10) // 2
    center_y = (height / 12 * 2 - height / 50 * 8) // 2

    font = pygame.font.SysFont("dejavusans", width // 10)
    text = "level "
    text = font.render(text, False, [0, 0, 0])
    screen.blit(text, [width // 12 + width // 200 + width // 12 * 4, height // 40 + height // 200 + height // 12 * 4])
    font = pygame.font.SysFont("dejavusans", width // 100 * 15)
    text_2 = str(level)
    text_2 = font.render(text_2, False, [0, 0, 0])

    if level > 9:
        screen.blit(text_2, [width // 12 + width // 12 * 55 // 100 + width // 12 * 4, height // 40 + height // 12 * 5])
    else:
        screen.blit(text_2, [width // 12 + width // 15 + width // 12 * 4, height // 40 + height // 12 * 5])

    screen.blit(red_player_image, (width // 12 + center_x + red_pos[0] * (width // 12 * 10) // 5,
                                   height // 40 + center_y + red_pos[1] * (height // 12 * 10) // 5))

    if len(purple_pos) != 1:
        screen.blit(purple_player_image, (width // 12 + center_x + purple_pos[0] * (width // 12 * 10) // 5,
                                          height // 40 + 3 * center_y + purple_pos[1] * (height // 12 * 10) // 5))
    if len(orange_pos) != 1:
        screen.blit(orange_player_image, (width // 12 + center_x + orange_pos[0] * (width // 12 * 10) // 5,
                                          height // 40 + center_y + orange_pos[1] * (height // 12 * 10) // 5))
    if len(green_pos) != 1:
        screen.blit(green_player_image, (width // 12 + center_x + green_pos[0] * (width // 12 * 10) // 5,
                                         height // 40 + center_y + green_pos[1] * (height // 12 * 10) // 5))
    if len(yellow_pos) != 1:
        screen.blit(yellow_player_image, (width // 12 + center_x + yellow_pos[0] * (width // 12 * 10) // 5,
                                          height // 40 + center_y + yellow_pos[1] * (height // 12 * 10) // 5))
    if len(blue_pos) != 1:
        screen.blit(blue_player_image, (width // 12 + center_x + blue_pos[0] * (width // 12 * 10) // 5,
                                        height // 40 + center_y + blue_pos[1] * (height // 12 * 10) // 5))

    if moves_num > 0:
        back_to_start_image = pygame.image.load("resources/images/back_to_start.png")
        back_to_start_image = pygame.transform.scale(back_to_start_image, (width // 8, height // 10))
        screen.blit(back_to_start_image, (width // 12 * 3, 2 * height // 40 + height // 12 * 10))

        move_back_image = pygame.image.load("resources/images/move_back.png")
        move_back_image = pygame.transform.scale(move_back_image, (width // 12, height // 10))
        screen.blit(move_back_image, (width // 12 * 5, 2 * height // 40 + height // 12 * 10))

    if deleted_moves_num > 0:
        move_forward_image = pygame.image.load("resources/images/move_forward.png")
        move_forward_image = pygame.transform.scale(move_forward_image, (width // 12, height // 10))
        screen.blit(move_forward_image, (width // 12 * 7, 2 * height // 40 + height // 12 * 10))

        last_forward_image = pygame.image.load("resources/images/last_forward.png")
        last_forward_image = pygame.transform.scale(last_forward_image, (width // 8, height // 10))
        screen.blit(last_forward_image, (width // 12 * 7 + width // 8, 2 * height // 40 + height // 12 * 10))


def optional_moves_append_to_screen(screen, optional_moves, red_position, purple_position, orange_position,
                                    green_position, yellow_position, blue_position, active_player):
    right_arrow = pygame.image.load("resources/images/right_arrow.png")
    right_arrow = pygame.transform.scale(right_arrow, (width // 24, height // 24))
    left_arrow = pygame.image.load("resources/images/left_arrow.png")
    left_arrow = pygame.transform.scale(left_arrow, (width // 24, height // 24))
    down_arrow = pygame.image.load("resources/images/down_arrow.png")
    down_arrow = pygame.transform.scale(down_arrow, (width // 24, height // 24))
    up_arrow = pygame.image.load("resources/images/up_arrow.png")
    up_arrow = pygame.transform.scale(up_arrow, (width // 24, height // 24))
    if active_player == 'red':
        active_pos = red_position
    elif active_player == 'purple':
        active_pos = purple_position
    elif active_player == 'orange':
        active_pos = orange_position
    elif active_player == 'green':
        active_pos = green_position
    elif active_player == 'yellow':
        active_pos = yellow_position
    elif active_player == 'blue':
        active_pos = blue_position
    else:
        active_pos = [-1]
    for i in range(len(optional_moves)):
        if optional_moves[i][0] == active_pos:
            if optional_moves[i][1] == 0:
                if optional_moves[i][2] > 0:
                    screen.blit(right_arrow,
                                (width // 12 - width // 24 + width // 12 * 2 * optional_moves[i][0][
                                    0] + width // 12 * 2,
                                 height // 40 + 2 * height // 12 * optional_moves[i][0][
                                     1] + height // 12 - height // 24 // 2))
                else:
                    screen.blit(left_arrow,
                                (width // 12 + width // 12 * 2 * optional_moves[i][0][0],
                                 height // 40 + 2 * height // 12 * optional_moves[i][0][
                                     1] + height // 12 - height // 24 // 2))
            else:
                if optional_moves[i][2] > 0:
                    screen.blit(down_arrow,
                                (width // 12 - width // 24 // 2 + width // 12 * 2 * optional_moves[i][0][
                                    0] + width // 12,
                                 height // 40 + height // 12 * 2 - height // 24 + 2 * height // 12 *
                                 optional_moves[i][0][
                                     1]))
                else:
                    screen.blit(up_arrow,
                                (width // 12 - width // 24 // 2 + width // 12 * 2 * optional_moves[i][0][
                                    0] + width // 12,
                                 height // 40 + 2 * height // 12 *
                                 optional_moves[i][0][
                                     1]))


def game(screen):
    instructions_3 = -2
    instructions_2 = -1
    instructions_1 = 0
    starting = 1
    choose_level = 2
    chosen_level = 3
    state = starting
    players_images = init_players()
    mouse_pressed = 0

    board = []
    red_position = []
    purple_position = []
    orange_position = []
    green_position = []
    yellow_position = []
    blue_position = []
    active_player = 'none'
    moves = []
    deleted_moves = []
    the_level = 0
    movement = ['none', 1, 0]
    side_of_touch = 0
    direction_move = True

    while True:
        # update the screen
        pygame.display.flip()
        # clear the screen before drawing it again
        screen.fill([255, 255, 255])
        # get events from user and use them
        events = pygame.event.get()
        use_events(events)
        # get mouse values
        last_press = mouse_pressed
        mouse_pressed, x_mouse, y_mouse = get_mouse_clicked_pos()

        if state >= starting:
            background_image = pygame.image.load("resources/images/background.png")
            background_image = pygame.transform.scale(background_image, (width, height))
            screen.blit(background_image, (0, 0))

        if state == starting:
            starting_screen(screen, players_images)
            if mouse_pressed == 0 and last_press == 1:
                if abs(x_mouse - width // 2) < width // 4:
                    if abs(y_mouse - height // 5.5) < height // 8:
                        state += 1
                    elif abs(y_mouse - height // (650 / 320)) < height // 16:
                        state -= 1
        elif state < starting:
            if state == instructions_3:
                third_instructions_screen(screen)
            elif state == instructions_2:
                second_instructions_screen(screen)
            elif state == instructions_1:
                first_instructions_screen(screen)
            if state != instructions_3:
                arrow = pygame.image.load("resources/images/right_arrow.png")
                arrow = pygame.transform.scale(arrow, (width // 8, height // 8))
                screen.blit(arrow, (width // 8 * 7, height // 8 * 7))

            home = pygame.image.load("resources/images/home.png")
            home = pygame.transform.scale(home, (width // 8, height // 8))
            screen.blit(home, (3, height // 8 * 7))
            if mouse_pressed == 0 and last_press == 1:
                if abs(y_mouse - height // 16 * 15) < height // 16:
                    if x_mouse < width // 8:
                        state = starting
                    elif x_mouse > width // 8 * 7 and state != instructions_3:
                        state -= 1
        else:
            if state == choose_level:
                choose_level_screen(screen, players_images)
                if mouse_pressed == 0 and last_press == 1:
                    if y_mouse < height // 8 * 5:
                        the_level = (8 * y_mouse // height * 8) + (x_mouse // (width // 8) + 1)
                        print('the level you choose is level ', the_level)
                        board = [[0 for i in range(5)] for j in range(5)]
                        first_positions = init_levels()
                        red_position = first_positions[0][the_level - 1]
                        purple_position = first_positions[1][the_level - 1]
                        orange_position = first_positions[2][the_level - 1]
                        green_position = first_positions[3][the_level - 1]
                        yellow_position = first_positions[4][the_level - 1]
                        blue_position = first_positions[5][the_level - 1]

                        board[red_position[0]][red_position[1]] = 1
                        if len(purple_position) != 1:
                            board[purple_position[0]][purple_position[1]] = 1
                        if len(orange_position) != 1:
                            board[orange_position[0]][orange_position[1]] = 1
                        if len(green_position) != 1:
                            board[green_position[0]][green_position[1]] = 1
                        if len(yellow_position) != 1:
                            board[yellow_position[0]][yellow_position[1]] = 1
                        if len(blue_position) != 1:
                            board[blue_position[0]][blue_position[1]] = 1
                        active_player = 'none'
                        moves = []
                        state += 1
            elif state == chosen_level:
                optional_moves = optional_move(board)
                if red_position == [2, 2]:
                    optional_moves = []
                level_screen(screen, red_position, purple_position, orange_position, green_position, yellow_position,
                             blue_position, players_images, len(moves), len(deleted_moves), the_level)
                if movement[2] != 0:
                    if movement[0] == 'red':
                        if movement[1] == 0:
                            tnai = abs(movement[2] + side_of_touch * 0.4) > 0.05
                        else:
                            tnai = abs(movement[2] + side_of_touch * 0.1) > 0.05
                        if tnai and direction_move:
                            red_position[movement[1]] += (movement[2] + side_of_touch * 1.3) / 10
                            movement[2] -= (movement[2] + side_of_touch * 1.3) / 10
                        elif abs(movement[2]) > 0.02:
                            direction_move = False
                            red_position[movement[1]] += movement[2] / 10
                            movement[2] -= movement[2] / 10
                        else:
                            direction_move = True
                            red_position[movement[1]] += movement[2]
                            red_position[movement[1]] = round(red_position[movement[1]])
                            movement[2] = 0
                else:
                    optional_moves_append_to_screen(screen, optional_moves, red_position, purple_position, orange_position,
                                                    green_position, yellow_position, blue_position, active_player)

                    if mouse_pressed == 0 and last_press == 1:
                        if abs(y_mouse - (height // 40 + height // 12 * 5)) <= height // 12 * 5:
                            if abs(x_mouse - (width // 12 * 6)) <= width // 12 * 5:
                                touched_pos = [0, 0]
                                touched_pos[0] = (x_mouse - width // 12) // (width // 12 * 2)
                                touched_pos[1] = (y_mouse - height // 40) // (height // 12 * 2)

                                if touched_pos == red_position:
                                    if active_player != 'red':
                                        active_player = 'red'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            print("moving")
                                            moves.append(moving)
                                            board[red_position[0]][red_position[1]] = 0
                                            movement = ['red', moving[1], moving[2]]
                                            side_of_touch = round(movement[2] // abs(movement[2]))
                                            red_position[moving[1]] += moving[2]
                                            board[red_position[0]][red_position[1]] = 1
                                            deleted_moves = []
                                            red_position[moving[1]] -= moving[2]
                                        active_player = 'none'
                                elif touched_pos == purple_position:
                                    if active_player != 'purple':
                                        active_player = 'purple'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            moves.append(moving)
                                            board[purple_position[0]][purple_position[1]] = 0
                                            purple_position[moving[1]] += moving[2]
                                            board[purple_position[0]][purple_position[1]] = 1
                                            deleted_moves = []
                                        active_player = 'none'
                                elif touched_pos == orange_position:
                                    if active_player != 'orange':
                                        active_player = 'orange'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            moves.append(moving)
                                            board[orange_position[0]][orange_position[1]] = 0
                                            orange_position[moving[1]] += moving[2]
                                            board[orange_position[0]][orange_position[1]] = 1
                                            deleted_moves = []
                                        active_player = 'none'
                                elif touched_pos == green_position:
                                    if active_player != 'green':
                                        active_player = 'green'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            moves.append(moving)
                                            board[green_position[0]][green_position[1]] = 0
                                            green_position[moving[1]] += moving[2]
                                            board[green_position[0]][green_position[1]] = 1
                                            deleted_moves = []
                                        active_player = 'none'
                                elif touched_pos == yellow_position:
                                    if active_player != 'yellow':
                                        active_player = 'yellow'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            moves.append(moving)
                                            board[yellow_position[0]][yellow_position[1]] = 0
                                            yellow_position[moving[1]] += moving[2]
                                            board[yellow_position[0]][yellow_position[1]] = 1
                                            deleted_moves = []
                                        active_player = 'none'
                                elif touched_pos == blue_position:
                                    if active_player != 'blue':
                                        active_player = 'blue'
                                    else:
                                        moving = touch_movement_arrow(x_mouse, y_mouse, touched_pos, optional_moves)
                                        if moving[2] < 10:
                                            moves.append(moving)
                                            board[blue_position[0]][blue_position[1]] = 0
                                            blue_position[moving[1]] += moving[2]
                                            board[blue_position[0]][blue_position[1]] = 1
                                            deleted_moves = []
                                        active_player = 'none'
                        elif abs(y_mouse - (
                                2 * height // 40 + height // 12 * 10 + height // 10 // 2)) <= height // 10 // 2:
                            if abs(x_mouse - (width // 12 * 3 + width // 8 // 2)) <= width // 8 // 2 and len(moves) > 0:
                                active_player = 'none'
                                while len(moves) > 0:
                                    last_pos = moves[-1][0]
                                    board[last_pos[0]][last_pos[1]] = 1
                                    index_changes = moves[-1][2]
                                    changed_index = moves[-1][1]
                                    last_pos[changed_index] += index_changes
                                    board[last_pos[0]][last_pos[1]] = 0
                                    if last_pos == red_position:
                                        red_position[moves[-1][1]] -= moves[-1][2]
                                    if last_pos == purple_position:
                                        purple_position[moves[-1][1]] -= moves[-1][2]
                                    if last_pos == orange_position:
                                        orange_position[moves[-1][1]] -= moves[-1][2]
                                    if last_pos == green_position:
                                        green_position[moves[-1][1]] -= moves[-1][2]
                                    if last_pos == yellow_position:
                                        yellow_position[moves[-1][1]] -= moves[-1][2]
                                    if last_pos == blue_position:
                                        blue_position[moves[-1][1]] -= moves[-1][2]
                                    moves[-1][0][changed_index] -= index_changes
                                    deleted_moves.append(moves[-1])
                                    moves.remove(moves[-1])
                            elif abs(x_mouse - (width // 12 * 5 + width // 12 // 2)) <= width // 12 // 2 and len(moves) > 0:
                                active_player = 'none'
                                last_pos = moves[-1][0]
                                board[last_pos[0]][last_pos[1]] = 1
                                index_changes = moves[-1][2]
                                changed_index = moves[-1][1]
                                last_pos[changed_index] += index_changes
                                board[last_pos[0]][last_pos[1]] = 0
                                if last_pos == red_position:
                                    red_position[moves[-1][1]] -= moves[-1][2]
                                if last_pos == purple_position:
                                    purple_position[moves[-1][1]] -= moves[-1][2]
                                if last_pos == orange_position:
                                    orange_position[moves[-1][1]] -= moves[-1][2]
                                if last_pos == green_position:
                                    green_position[moves[-1][1]] -= moves[-1][2]
                                if last_pos == yellow_position:
                                    yellow_position[moves[-1][1]] -= moves[-1][2]
                                if last_pos == blue_position:
                                    blue_position[moves[-1][1]] -= moves[-1][2]
                                moves[-1][0][changed_index] -= index_changes
                                deleted_moves.append(moves[-1])
                                moves.remove(moves[-1])
                            elif abs(x_mouse - (width // 12 * 7 + width // 12 // 2)) <= width // 12 // 2 and len(
                                    deleted_moves) > 0:
                                active_player = 'none'
                                last_pos = deleted_moves[-1][0]
                                board[last_pos[0]][last_pos[1]] = 0
                                changed_index = deleted_moves[-1][1]
                                index_changes = deleted_moves[-1][2]
                                if last_pos == red_position:
                                    red_position[changed_index] += index_changes
                                elif last_pos == purple_position:
                                    purple_position[changed_index] += index_changes
                                elif last_pos == orange_position:
                                    orange_position[changed_index] += index_changes
                                elif last_pos == green_position:
                                    green_position[changed_index] += index_changes
                                elif last_pos == yellow_position:
                                    yellow_position[changed_index] += index_changes
                                elif last_pos == blue_position:
                                    blue_position[changed_index] += index_changes
                                last_pos[changed_index] += index_changes
                                board[last_pos[0]][last_pos[1]] = 1
                                deleted_moves[-1][0][changed_index] -= index_changes
                                moves.append(deleted_moves[-1])
                                deleted_moves.remove(deleted_moves[-1])
                            elif abs(x_mouse - (
                                    width // 12 * 8 + width // 12 // 2 + width // 8 // 2)) <= width // 8 // 2 and len(
                                    deleted_moves) > 0:
                                active_player = 'none'
                                while len(deleted_moves) > 0:
                                    last_pos = deleted_moves[-1][0]
                                    board[last_pos[0]][last_pos[1]] = 0
                                    changed_index = deleted_moves[-1][1]
                                    index_changes = deleted_moves[-1][2]
                                    if last_pos == red_position:
                                        red_position[changed_index] += index_changes
                                    elif last_pos == purple_position:
                                        purple_position[changed_index] += index_changes
                                    elif last_pos == orange_position:
                                        orange_position[changed_index] += index_changes
                                    elif last_pos == green_position:
                                        green_position[changed_index] += index_changes
                                    elif last_pos == yellow_position:
                                        yellow_position[changed_index] += index_changes
                                    elif last_pos == blue_position:
                                        blue_position[changed_index] += index_changes
                                    last_pos[changed_index] += index_changes
                                    board[last_pos[0]][last_pos[1]] = 1
                                    deleted_moves[-1][0][changed_index] -= index_changes
                                    moves.append(deleted_moves[-1])
                                    deleted_moves.remove(deleted_moves[-1])

        if state != starting:
            home = pygame.image.load("resources/images/home.png")
            home = pygame.transform.scale(home, (width // 8, height // 8))
            screen.blit(home, (3, height // 8 * 7))
            if mouse_pressed == 0 and last_press == 1:
                if abs(y_mouse - height // 16 * 15) < height // 16 and x_mouse < width // 8:
                    state = starting


if __name__ == '__main__':
    main()
