import pygame

pygame.init()

win = pygame.display.set_mode((900, 900))
pygame.display.set_caption("sudoku-solver")

solving = False

def draw():
    win.fill([255, 255, 255])
    for i in range(9):
        pygame.draw.rect(win, (0, 0, 0), (0 + i * 100, 0, 5, 900))
        pygame.draw.rect(win, (0, 0, 0), (0, 0 + i * 100, 900, 5))
    for i in range(3):
        pygame.draw.rect(win, (0, 0, 0), (0 + i * 300, 0, 10, 900))
        pygame.draw.rect(win, (0, 0, 0), (0, 0 + i * 300, 900, 10))

font = pygame.font.SysFont("comicsansms", 125)

draw()
x_pos = 0
y_pos = 0

while solving == False:
    number = 0
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            x_pos = x_pos - (x_pos % 100)
            y_pos = y_pos - (y_pos % 100)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                number = 1
            elif event.key == pygame.K_2:
                number = 2
            elif event.key == pygame.K_3:
                number = 3
            elif event.key == pygame.K_4:
                number = 4
            elif event.key == pygame.K_5:
                number = 5
            elif event.key == pygame.K_6:
                number = 6
            elif event.key == pygame.K_7:
                number = 7
            elif event.key == pygame.K_8:
                number = 8
            elif event.key == pygame.K_9:
                number = 9
    if number != 0 and x_pos != 0:
        pygame.draw.rect(win, (255, 255, 255), (x_pos + 10, y_pos + 10, 80, 80))
        text = font.render(str(number), True, (0, 0, 0))

        win.blit(text,
                 (x_pos + 30, y_pos + 17))

    pygame.display.update()
