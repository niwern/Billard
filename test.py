import draw, color, pygame

image = pygame.image.load("cat Kopie.jpg")
w = 600
h = 400
image = pygame.transform.rotozoom(image, 0, 0.25)

LION_3000 = pygame.image.load("lion 3000.jpg")
LION_3000 = pygame.transform.rotozoom(LION_3000, 0, 0.1)

def main():
    draw.set_canvas_size(image, w, h)
    while True:
        # pygame.init()

        #draw.rectangle(0.1, 0.1, .2, .2)
        #draw.picture(LION_3000, 2832, 1913)
        draw.picture_improved(LION_3000, 20, 20)

        draw.show(1)
        #draw.clear(image)


if __name__ == "__main__":
    main()
