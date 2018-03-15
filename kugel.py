import draw
import color
import vektor
import math, sys

RADIUS = 0.015

class kugel(object):
    def __init__(self, x, y, c, num, m):
        """
        :param x: x-Position
        :param y: y-Position
        :param c: Farbe
        :param num: Zahl, die angezeigt wird
        :param m: Marker
        :param v_x: x-Anfangsgeschwindigkeit
        :param v_y: y-Anfangsgeschwindigkeit
        """
        self.x = x
        self.y = y
        self.c = c
        self.m = m
        self.num = num
        self.v = vektor.vektor(0, 0)
        self.eingelocht = False


    def draw(self):
        """
        zeichent die Kugel
        :return:
        """
        draw.set_pen_color(self.c)
        draw.filled_circle(self.x, self.y, RADIUS)
        if self.m:
            draw.set_pen_color(color.WHITE)
            draw.filled_diamond(self.x, self.y, RADIUS/2)
        draw.set_font_size()
        draw.set_font_family()
        # draw.text(self.x, self.y, self.num) todo wahrscheinlich nich moeglich, durch Bug

    def move(self, time=1, friction=True):
        """
        bewegt die Kugel
        :param time: Zeit in Millisekunden
        :param friction: Reibung (bool)
        :return:
        """
        self.x, self.y = self.new_position(time)
        if friction:  # bei Reibung
            self.v *= .98

    def new_position(self, time=1):
        """
        Berechnet die neue Position der Kugel
        :return new_x, new_y:
        """
        new_x = self.x + self.v.x*time
        new_y = self.y + self.v.y*time
        return new_x, new_y

    def einlochen(self, current_player, p):
        print("kugel {} mit {} wurde eingelocht".format(self.c, self.m))

        if self.c == color.BLACK:
            if current_player.points == 7:
                print("{} hat gewonnen.".format(current_player.name))
            else:
                print("{} hat verloren.".format(current_player.name))
            sys.exit()

        if current_player.marker == None and self.c != color.WHITE:
            if p[0].name == current_player.name:
                p[0].marker = self.m
                p[1].marker = not self.m
            else:
                p[0].marker = not self.m
                p[1].marker = self.m

            print(p[0].marker, p[1].marker)
        if self.c != color.WHITE:
            if self.m == p[0].marker:
                p[0].get_point()
            else:
                p[1].get_point()
            if p[0].name == current_player.name and p[0].ist_am_zug:
                p[0].ist_am_zug = False
                p[1].ist_am_zug = True


        self.eingelocht = True
        self.v = vektor.vektor(0, 0)
        self.x = 0.5
        self.y = 0.5

    def overlap(self, list):
        for el in list:
            if math.hypot(el.x - self.x, el.y - self.y) < 2*RADIUS:
                return True
        return False
