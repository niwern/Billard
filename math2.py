import pygame
import draw
draw.set_canvas_size(600, 600)
while True:
    if draw.has_next_key_typed():
        draw.next_key_typed()
