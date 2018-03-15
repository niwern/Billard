import draw
import kugel
import vektor
import math
import color

PEN_RADIUS = 0.007
LENGTH = 30


class cue(object):
    def __init__(self):
        self.alpha = 0
        self.pow = 1

    def rotate(self):
        if self.alpha >= math.pi:
            self.alpha -= 2*math.pi
        self.alpha += 0.01

    def power(self, k, cue_power):
        v = vektor.vektor((k.x + math.cos(self.alpha)) - (k.x + math.cos(self.alpha)*2),
                          (k.y + math.sin(self.alpha)) - (k.y + math.sin(self.alpha)*2))
        v *= .05
        v *= cue_power
        return v

    def draw(self, k):
        draw.set_pen_radius(PEN_RADIUS)
        draw.set_pen_color(color.BROWN)
        draw.line(k.x + math.cos(self.alpha)*kugel.RADIUS*(2 + self.pow),
                  k.y + math.sin(self.alpha)*kugel.RADIUS*(2 + self.pow),
                  k.x + math.cos(self.alpha)*kugel.RADIUS*(LENGTH + self.pow),
                  k.y + math.sin(self.alpha)*kugel.RADIUS*(LENGTH + self.pow))
        draw.set_pen_radius(0.001)
        draw.set_pen_color(color.RED)
        draw.line(k.x - math.cos(self.alpha)*kugel.RADIUS*(2),
                  k.y - math.sin(self.alpha)*kugel.RADIUS*(2),
                  k.x - math.cos(self.alpha)*kugel.RADIUS*(600),
                  k.y - math.sin(self.alpha)*kugel.RADIUS*(600))
