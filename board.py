import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[None for i in range(9)] for j in range(9)]

    def draw(self):
        cell_w = self.width // 9
        cell_h = self.height // 9
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 3
            else:
                line_thickness = 1

            # horizontal
            pygame.draw.line(
                self.screen,
                'black',
                (0, i * cell_h),
                (self.width, i * cell_h),
                line_thickness
            )

            # vertical
            pygame.draw.line(
                self.screen,
                'black',
                (i * cell_w, 0),
                (i * cell_w, self.height),
                line_thickness
            )

            for i in self.cells:
                for cell in i:
                    cell.draw(self.screen)


    def select(self, row, col):
        pass

    def click(self, row, col):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, number):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
