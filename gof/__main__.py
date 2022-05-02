import argparse
from .game import GameOfLife

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, help='Width of the grid', required=True)
parser.add_argument('--height', type=int, help='Height of the grid', required=True)
parser.add_argument('--size', type=int, help='Size of the cells', default=10)
parser.add_argument('--fps', type=int, help='FPS of the game', default=60)
parser.add_argument('--random', action='store_true', help='Randomize the grid', default=False)
args = parser.parse_args()

game = GameOfLife(args.width, args.height, args.size, args.fps)
if args.random:
    game.random_init()
game.run()  
