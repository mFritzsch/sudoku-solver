import pygame


def draw(win):
    pygame.display.set_caption("sudoku-solver")
    win.fill([255, 255, 255])
    for i in range(9):
        pygame.draw.rect(win, (0, 0, 0), (0 + i * 100, 0, 5, 900))
        pygame.draw.rect(win, (0, 0, 0), (0, 0 + i * 100, 900, 5))
    for i in range(3):
        pygame.draw.rect(win, (0, 0, 0), (0 + i * 300, 0, 10, 900))
        pygame.draw.rect(win, (0, 0, 0), (0, 0 + i * 300, 900, 10))


def fill(win, font):
    board = [0] * 81
    while True:
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
                elif event.key == pygame.K_RETURN:
                    return board
        if number != 0 and x_pos != -15:
            board[int(x_pos / 100 * 9 + y_pos / 100)] = number
            pygame.draw.rect(win, (255, 255, 255), (x_pos + 10, y_pos + 10, 80, 80))
            text = font.render(str(number), True, (0, 0, 0))

            win.blit(text,
                     (x_pos + 30, y_pos + 17))

        pygame.display.update()


def solve(X, Y, solution):
    # Step 1—checks, if matrix is empty, otherwise proceeds.
    if not X:
        return solution, True
    # chooses a column
    lowest_number = min(X)
    # iterates through row
    for row in X[lowest_number]:
        # includes column in partial solution
        if Y[row]:
            solution.append(row)
            next_Y = Y.copy()
            next_X = X.copy()
            for i in Y[row]:
                for j in Y:
                    for k in Y[j]:
                        if k == i:
                            next_Y[j] = []
                next_X.pop(i)
            if type(next_Y) == dict:
                solution, solved = solve(next_X, next_Y, solution)
                if solved:
                    return solution, solved
            else:
                solution.pop(-1)
                return solution, False
    solution.pop(-1)
    return solution, False


def convert(board):
    X = {}
    for i in range(81):
        list = []
        for j in range(9):
            list.append(i * 9 + j + 1)
        X[i+1] = list
    for i in range(9):
        for j in range(9):
            list = []
            for k in range(9):
                list.append(k * 9 + 1 + j + i * 81)
            X[82 + i * 9 + j] = list
    for i in range(81):
        list = []
        for j in range(9):
            list.append(1 * (81 * j) + 1 + i)
        X[163 + i] = list
    for i in range(81):
        list = []
        if i < 9:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i)
        elif i < 18:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 18)
        elif i < 27:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 36)
        elif i < 36:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 216)
        elif i < 45:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 234)
        elif i < 54:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 252)
        elif i < 63:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 432)
        elif i < 72:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 450)
        elif i < 81:
            for j in range(3):
                for k in range(3):
                    list.append(j * 81 + 1 + k * 9 + i + 468)
        X[244 + i] = list
    Y = {}
    for i in range(729):
        Y[i+1] = []
    for i in X:
        for j in X[i]:
            Y[j].append(i)

    next_Y = Y.copy()
    next_X = X.copy()
    list = []
    for i in range(len(board)):
        if board[i] != 0:
            list.append(i * 9 + board[i])
    for l in list:
        for i in next_Y[l]:
            for j in next_Y:
                for k in next_Y[j]:
                    if k == i:
                        next_Y[j] = []
            next_X.pop(i)
    for i in range(len(list)):
        list[i] = list[i] / 9
    return next_X, next_Y


def process_solution(solution, win, font):
    for i in range(len(solution)):
        number = solution[i] % 9
        if number == 0:
            number = 9
        x_pos = int((solution[i] - number) / 81) * 100
        y_pos = (((solution[i] - number) / 9) % 9) * 100
        pygame.draw.rect(win, (255, 255, 255), (x_pos + 10, y_pos + 10, 80, 80))
        text = font.render(str(number), True, (0, 0, 0))

        win.blit(text,
                 (x_pos + 30, y_pos + 17))

        pygame.display.update()


def sudoku_solver():
    pygame.init()
    win = pygame.display.set_mode((900, 900))
    font = pygame.font.SysFont("comicsansms", 125)
    draw(win)
    while True:
        board = fill(win, font)
        X, Y = convert(board)
        solution = solve(X, Y, [])[0]
        process_solution(solution, win, font)


sudoku_solver()
