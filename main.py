from game import GameOfLife


if __name__ == '__main__':
    game = GameOfLife(600, 600)
    game.random_init()
    game.run()