import pygame
import numpy as np

class GameOfLife:

    def __init__(self, width, height, cell_size=10):
        self.cells_size = cell_size

        self.color_bg = (10, 10, 10)
        self.color_grid = (40, 40, 40)
        self.color_die = (170, 170, 170)
        self.color_alive = (255, 255, 255)

        self.cells = np.zeros((height//cell_size, width//cell_size))
        self.running = False

        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(self.color_grid)
        self.update()
        pygame.display.flip()
        pygame.display.update()

    def update(self, progress=False):
        update_cells = np.zeros((self.cells.shape[0], self.cells.shape[1]))

        for row, col in np.ndindex(self.cells.shape):
            alive = np.sum(self.cells[row-1:row+2, col-1:col+2]) - self.cells[row, col]
            color = self.color_bg if self.cells[row, col] == 0 else self.color_alive

            if self.cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    color = self.color_die if progress else color
                elif 2 <= alive <= 3:
                    update_cells[row, col] = 1
                    color = self.color_alive
            
            elif alive == 3:
                update_cells[row, col] = 1
                color = self.color_alive if progress else color

            pygame.draw.rect(self.screen, color, (col * self.cells_size, row * self.cells_size, self.cells_size - 1, self.cells_size - 1))
        return update_cells

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running
                        self.update()
                        pygame.display.update()

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // self.cells_size
                    col = pos[0] // self.cells_size
                    self.cells[row, col] = 1
                    self.update()
                    pygame.display.update()
            
            self.screen.fill(self.color_grid)

            if self.running:
                self.cells = self.update(True)
                pygame.display.update()