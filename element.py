import pygame

from settings import UNIT_LENGTH, UNIT_DISTANCE, MARGIN_X, MARGIN_Y, UNIT_Y_SCALE, UNIT_COLOR


class Element(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.image = pygame.Surface((UNIT_LENGTH, y * UNIT_Y_SCALE))
        self.image.fill(UNIT_COLOR)

        self.rect = self.image.get_rect(topleft=
                                        (MARGIN_X + x * (UNIT_LENGTH + UNIT_DISTANCE),
                                         MARGIN_Y - y * UNIT_Y_SCALE)
                                        )

    def __repr__(self):
        return f"<Elem Sprite with (x: {self.x}, y: {self.y})"

