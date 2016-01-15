from minesweeper import *

random.seed()


def game_loop():
    game = Minesweeper(game_width,game_height, bugx, bugy, mines)
    game.startboard()

    while not game.done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == game.mouse.LEFT:
                a, b = event.pos
                game.boardhover(a, b, 1)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == game.mouse.RIGHT:
                a, b = event.pos
                game.boardhover(a, b, 3)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.done = True

        printimg(background, 0, 0)
        game.updateboard()
        game.bug.update()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()


