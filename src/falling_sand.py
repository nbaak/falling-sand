#!/usr/bin/env python3

import pygame
import random
import datetime

from pixel import Pixel


def sand_fall(sand, persistent_sand, height, pixel_scale):
    for pxl in sand:
        x, y = pxl.pos
        l_d = x - 1, y + 1  # left down
        s_d = x, y + 1  # straight down
        r_d = x + 1, y + 1  # right down

        if y >= ((height - 1) // pixel_scale):
            pxl.final = True
            continue

        if s_d not in sand and s_d not in persistent_sand:
            pxl.pos = s_d

        elif l_d not in sand and r_d not in sand and l_d not in persistent_sand and r_d not in persistent_sand:
            pxl.pos = random.choice([l_d, r_d])

        elif l_d not in sand and l_d not in persistent_sand:
            pxl.pos = l_d

        elif r_d not in sand and r_d not in persistent_sand:
            pxl.pos = r_d

        elif r_d in sand and s_d in sand and l_d in sand and r_d in persistent_sand and s_d in persistent_sand and l_d in persistent_sand:
            pxl.final = True


def check_persistent(sand:list, persistent_sand:list, pixel_scale, max_height):
    for pxl in sand:
        if pxl.final:
            persistent_sand.append(pxl)
            sand.remove(pxl)


def take_screenshot(window):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    pygame.image.save(window, filename)
    print(f"Screenshot saved as {filename}")


def main():
    sand = []
    persistent_sand = []

    pygame.init()

    size = width, height = 800, 300

    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 30

    hue = 0
    pixel_scale = 10
    running = True

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_s:
                    take_screenshot(window)

        window.fill('black')

        if pygame.mouse.get_pressed()[0]:
            color = pygame.Color(0)
            hue = (hue + 1) % 360
            color.hsva = hue, 100, 100

            x, y = pygame.mouse.get_pos()
            sand.append(Pixel((x // pixel_scale, y // pixel_scale), color))

        for pxl in sand + persistent_sand:
            pygame.draw.rect(window, pxl.color, (pxl.pos[0] * pixel_scale, pxl.pos[1] * pixel_scale, pixel_scale, pixel_scale))

        sand_fall(sand, persistent_sand, height, pixel_scale)
        check_persistent(sand, persistent_sand, pixel_scale, height)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
