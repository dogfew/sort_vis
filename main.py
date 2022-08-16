import pygame

from element import Element

from sorts.shuffle import beautiful_shuffle
from control import func, default_func
from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, ARRAY_LENGTH, FPS, BACKGROUND_COLOR)


def do_array(lst):
    array = pygame.sprite.Group()
    for j, i in enumerate(lst):
        array.add(Element(j, i))

    return array


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    lst = list(range(ARRAY_LENGTH))
    generator = False
    array = do_array(lst)

    sorting = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN and not sorting:
                sorting = True
                generator = func.get(event.key, default_func)(lst)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and not sorting:
            generator = beautiful_shuffle(lst)
            sorting = True

        if sorting:
            try:
                lst = next(generator)
                array = do_array(lst)
            except StopIteration:
                sorting = False

        screen.fill(BACKGROUND_COLOR)
        array.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
