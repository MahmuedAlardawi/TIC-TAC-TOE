import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random

# Initialize the game board
board = [None] * 9
x_positions = []
o_positions = []
current_selection = 0  # Start at the top-left corner of the board
x_color = [random.random(), random.random(), random.random()]
o_color = [random.random(), random.random(), random.random()]


def init():
    glClearColor(0.8, 0.8, 0.8, 1.0)  # Set background color
    glEnable(GL_LINE_SMOOTH)
    glLineWidth(5)

def reset_board():
    global board, x_positions, o_positions, current_selection
    board = [None] * 9
    x_positions = []
    o_positions = []
    current_selection = 0

def draw_x(pos_x, pos_y):
    glColor3fv(x_color)  # Red color for X
    glBegin(GL_LINES)
    glVertex2f(pos_x - 0.2, pos_y - 0.2)
    glVertex2f(pos_x + 0.2, pos_y + 0.2)
    glVertex2f(pos_x - 0.2, pos_y + 0.2)
    glVertex2f(pos_x + 0.2, pos_y - 0.2)
    glEnd()

def draw_o(pos_x, pos_y):
    glColor3fv(o_color)  # Red color for O
    glBegin(GL_LINE_LOOP)
    for angle in range(360):
        rad = angle * 3.14159 / 180
        glVertex2f(pos_x + 0.2 * math.cos(rad), pos_y + 0.2 * math.sin(rad))
    glEnd()

def draw_board():
    glColor3f(0, 0, 0)  # Black color for board lines
    glBegin(GL_LINES)
    glVertex2f(-0.33, 1)
    glVertex2f(-0.33, -1)
    glVertex2f(0.33, 1)
    glVertex2f(0.33, -1)
    glVertex2f(-1, 0.33)
    glVertex2f(1, 0.33)
    glVertex2f(-1, -0.33)
    glVertex2f(1, -0.33)
    glEnd()

def draw_highlight():
    row, col = divmod(current_selection, 3)
    x = -0.66 + col * 0.66
    y = 0.66 - row * 0.66

    glColor3f(1, 1, 0)  # Yellow color for highlight
    glBegin(GL_QUADS)
    glVertex2f(x - 0.33, y + 0.33)
    glVertex2f(x + 0.33, y + 0.33)
    glVertex2f(x + 0.33, y - 0.33)
    glVertex2f(x - 0.33, y - 0.33)
    glEnd()

def update_board(player):
    global x_positions, o_positions
    if board[current_selection] is None:
        board[current_selection] = player
        if player == 'X':
            x_positions.append(current_selection)
            if len(x_positions) > 3:
                oldest_x = x_positions.pop(0)
                board[oldest_x] = None
        elif player == 'O':
            o_positions.append(current_selection)
            if len(o_positions) > 3:
                oldest_o = o_positions.pop(0)
                board[oldest_o] = None

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] is not None and board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]]
    return None

def main():
    global current_selection
    pygame.init()
    display = (300, 300)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(-1, 1, -1, 1)
    init()
    running = True
    player = 'X'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_selection % 3 < 2:
                    current_selection += 1
                elif event.key == pygame.K_LEFT and current_selection % 3 > 0:
                    current_selection -= 1
                elif event.key == pygame.K_UP and current_selection > 2:
                    current_selection -= 3
                elif event.key == pygame.K_DOWN and current_selection < 6:
                    current_selection += 3
                elif event.key == pygame.K_SPACE:
                    if check_win() or None not in board:
                        reset_board()
                    else:

                        if check_win() or not board[current_selection] is None:
                            continue  # Skip flipping player if game is won or board is full
                        update_board(player)
                        player = 'O' if player == 'X' else 'X'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_board()
        draw_highlight()  # Highlight the current selected cell
        for i in range(9):
            if board[i] == 'X':
                draw_x(-0.66 + (i % 3) * 0.66, 0.66 - (i // 3) * 0.66)
            elif board[i] == 'O':
                draw_o(-0.66 + (i % 3) * 0.66, 0.66 - (i // 3) * 0.66)

        winner = check_win()
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()