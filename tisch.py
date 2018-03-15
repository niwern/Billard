import draw
import color
import math
import kugel
import vektor
import cue
import player

# Konstanten
BORDER = .045  # Breite des Randes
LOCH_NORM = BORDER/math.sqrt(2)  # Konstante (wichtig, um Loecher zu zeichen)
BORDER_LOSS = .9  # Geschwindigkeitsverlust, bei Kollision mit Rand
KUGEL_NORM = math.sqrt(3)*kugel.RADIUS  # Konstante (wichtig, um Kugeln zu platzieren)

SAFE_SPACE = .0005


Y_MID = 0.5 + BORDER/2  #
X_STR_1 = 0.25 + BORDER/2  #
X_STR_2 = 0.75 - BORDER/2  #

p = [
    player.player("Player A"),
    player.player("Player B")
]

k = [  # Menge aller Kugeln
    kugel.kugel(X_STR_2, Y_MID, color.WHITE, " ", False)
]


def kugeln_legen():
    # k.append(kugel.kugel(X_STR_2, 0.65, color.BOOK_LIGHT_BLUE, " ", False))

    k.append(kugel.kugel(X_STR_1, Y_MID, color.RED, "1", True))

    k.append(
            kugel.kugel(X_STR_1 - SAFE_SPACE - KUGEL_NORM, Y_MID + (kugel.RADIUS + SAFE_SPACE), color.BLUE, "1", False))
    k.append(kugel.kugel(X_STR_1 - SAFE_SPACE - KUGEL_NORM, Y_MID - (kugel.RADIUS + SAFE_SPACE), color.PINK, "1", True))

    k.append(
            kugel.kugel(X_STR_1 - 2*SAFE_SPACE - 2*KUGEL_NORM, Y_MID + 2*(kugel.RADIUS + SAFE_SPACE), color.DARK_GREEN,
                        "1",
                        True))
    k.append(kugel.kugel(X_STR_1 - 2*SAFE_SPACE - 2*KUGEL_NORM, Y_MID, color.BLACK, "1", False))
    k.append(
            kugel.kugel(X_STR_1 - 2*SAFE_SPACE - 2*KUGEL_NORM, Y_MID - 2*(kugel.RADIUS + SAFE_SPACE), color.VIOLET, "1",
                        False))

    k.append(
            kugel.kugel(X_STR_1 - 3*SAFE_SPACE - 3*KUGEL_NORM, Y_MID + 3*(kugel.RADIUS + SAFE_SPACE), color.YELLOW, "1",
                        False))
    k.append(
            kugel.kugel(X_STR_1 - 3*SAFE_SPACE - 3*KUGEL_NORM, Y_MID + (kugel.RADIUS + SAFE_SPACE), color.BLUE, "1",
                        True))
    k.append(
            kugel.kugel(X_STR_1 - 3*SAFE_SPACE - 3*KUGEL_NORM, Y_MID - (kugel.RADIUS + SAFE_SPACE), color.DARK_GREEN,
                        "1",
                        False))
    k.append(
            kugel.kugel(X_STR_1 - 3*SAFE_SPACE - 3*KUGEL_NORM, Y_MID - 3*(kugel.RADIUS + SAFE_SPACE), color.ORANGE, "1",
                        True))

    k.append(
            kugel.kugel(X_STR_1 - 4*SAFE_SPACE - 4*KUGEL_NORM, Y_MID + 4*(kugel.RADIUS + SAFE_SPACE), color.VIOLET, "1",
                        True))
    k.append(
            kugel.kugel(X_STR_1 - 4*SAFE_SPACE - 4*KUGEL_NORM, Y_MID + 2*(kugel.RADIUS + SAFE_SPACE), color.ORANGE, "1",
                        False))
    k.append(kugel.kugel(X_STR_1 - 4*SAFE_SPACE - 4*KUGEL_NORM, Y_MID, color.YELLOW, "1", True))
    k.append(kugel.kugel(X_STR_1 - 4*SAFE_SPACE - 4*KUGEL_NORM, Y_MID - 2*(kugel.RADIUS + SAFE_SPACE), color.PINK, "1",
                         False))
    k.append(kugel.kugel(X_STR_1 - 4*SAFE_SPACE - 4*KUGEL_NORM, Y_MID - 4*(kugel.RADIUS + SAFE_SPACE), color.RED, "1",
                         False))


def tisch():
    """
    zeichnet den Tisch und die Kugeln
    :return:
    """
    # Table --------------------------------------------------------------------------------------
    draw.set_pen_color(color.GREEN)
    draw.filled_rectangle(0, 0.25, 1, 0.5)
    draw.set_pen_radius(BORDER)

    # Bande --------------------------------------------------------------------------------------
    draw.set_pen_color(color.BROWN)
    draw.filled_rectangle(0, .25, 1, BORDER)
    draw.filled_rectangle(0, .75, 1, BORDER)
    draw.filled_rectangle(0, .25, BORDER, 0.5)
    draw.filled_rectangle(1 - BORDER, .25, BORDER, 0.5)

    # Loecher ------------------------------------------------------------------------------------
    draw.set_pen_color(color.BLACK)

    # mittlere  -------------------------
    draw.filled_rectangle(.5 - BORDER/2, .25 + BORDER/2, BORDER, BORDER/2)
    draw.filled_rectangle(.5 - BORDER/2, .75, BORDER, BORDER/2)

    # rechts unten  ---------------------
    x1 = [BORDER/2, BORDER + LOCH_NORM, BORDER + LOCH_NORM, BORDER, BORDER/2, BORDER/2]
    y1 = [.25 + BORDER/2, .25 + BORDER/2, .25 + BORDER, .25 + BORDER + LOCH_NORM, .25 + BORDER + LOCH_NORM,
          .25 + BORDER/2]

    # links unten -----------------------
    x2 = []
    y2 = y1
    for x in x1:
        d = .5 - x
        x2.append(x + 2*d)

    # oben ------------------------------
    x3 = x1
    y3 = []
    x4 = x2
    y4 = []
    for y_1, y_2 in zip(y1, y2):
        d_1, d_2 = .5 + BORDER/2 - y_1, .5 + BORDER/2 - y_2
        y3.append(y_2 + 2*d_2)
        y4.append(y_1 + 2*d_1)

    # zeichnen --------------------------
    draw.filled_polygon(x1, y1)
    draw.filled_polygon(x2, y2)
    draw.filled_polygon(x3, y3)
    draw.filled_polygon(x4, y4)

    # Markierungen -------------------------------------------------------------------------------
    draw.set_pen_color(color.BLUE)
    for i in [0, 0.5]:
        for j in range(1, 4):
            draw.filled_diamond((.5 - BORDER)*j/4 + BORDER, .25 + BORDER/2 + i, BORDER/4)
        for j in range(1, 4):
            draw.filled_diamond((.5 - BORDER)*j/4 + 0.5, .25 + BORDER/2 + i, BORDER/4)
        for j in range(1, 4):
            draw.filled_diamond((BORDER/2 + 2*(i - (BORDER*i))), .25 + BORDER + (0.5 - BORDER)*j/4, BORDER/4)

    # Kugeln -------------------------------------------------------------------------------------
    for i in k:
        if not i.eingelocht:
            i.draw()


def collision_border(ball, current_player):  # TODO GENAUE BERECHNUNG
    """
    reflektiert die Kugeln, bei Kollision mit der Bande
    :param ball:
    :return:
    """

    new_x, new_y = ball.new_position()

    if new_x <= BORDER + kugel.RADIUS:
        time = (BORDER + kugel.RADIUS - ball.x)/ball.v.x
        ball.move(time, False)
        if 0.25 + BORDER + LOCH_NORM < ball.y < 0.75 - LOCH_NORM:
            ball.v.x *= -1*BORDER_LOSS
            ball.move((1 - time), True)
        else:
            ball.einlochen(current_player, p)
            new_x, new_y = .5, .5
    elif new_x >= 1 - kugel.RADIUS - BORDER:
        time = (1 - kugel.RADIUS - BORDER - ball.x)/ball.v.x
        ball.move(time, False)
        if 0.25 + BORDER + LOCH_NORM < ball.y < 0.75 - LOCH_NORM:
            ball.v.x *= -1*BORDER_LOSS
            ball.move((1 - time), True)
        else:
            ball.einlochen(current_player, p)
            new_x, new_y = .5, .5

    if new_y < .25 + BORDER + kugel.RADIUS:
        time = (.25 + BORDER + kugel.RADIUS - ball.y)/ball.v.y
        ball.move(time, False)
        if (BORDER + LOCH_NORM < ball.x < 0.5 - BORDER/2) or (0.5 + BORDER/2 < ball.x < 1 - (BORDER + LOCH_NORM)):
            ball.v.y *= -1*BORDER_LOSS
            ball.move((1 - time), True)
        else:
            ball.einlochen(current_player, p)
    elif new_y > .75 - kugel.RADIUS:
        time = (.75 - kugel.RADIUS - ball.y)/ball.v.y
        ball.move(time, False)
        if (BORDER + LOCH_NORM < ball.x < 0.5 - BORDER/2) or (0.5 + BORDER/2 < ball.x < 1 - (BORDER + LOCH_NORM)):
            ball.v.y *= -1*BORDER_LOSS
            ball.move((1 - time), True)
        else:
            ball.einlochen(current_player, p)
    """
    if ball.y < .25 + BORDER + kugel.RADIUS:
        ball.v.y *= -1
        ball.v *= BORDER_LOSS
    elif ball.y > .75 - kugel.RADIUS:
        ball.v.y *= -1
        ball.v *= BORDER_LOSS
    if ball.x < 0 + BORDER + kugel.RADIUS:
        ball.v.x *= -1
        ball.v *= BORDER_LOSS
    elif ball.x > 1 - kugel.RADIUS - BORDER:
        ball.v.x *= -1
        ball.v *= BORDER_LOSS"""


def next_collision(current, t=1):
    balls = k[:]

    for ball in balls:
        if ball == current:
            balls.remove(ball)

    pot_cot = []
    for i in balls:
        # zukuenftige Positionen der Kugeln errechnen --------------------------------------------
        c_x, c_y = current.new_position()
        i_x, i_y = i.new_position()

        if math.sqrt((c_x - i_x)**2 + (c_y - i_y)**2) <= 2*kugel.RADIUS and (
                i.v != vektor.vektor(0, 0) or current.v != vektor.vektor(0, 0) and not i.eingelocht):
            pot_cot.append(i)
    if pot_cot != []:
        _min = cal_time(current, pot_cot[0])
        _min_index = 0
        for j in range(1, len(pot_cot)):
            if cal_time(current, pot_cot[j]) < _min:
                _min = cal_time(current, pot_cot[j])
                _min_index = j
        kugel_collision(current, pot_cot[_min_index], t)
    current.move()


def kugel_collision(current, next, t):
    time = cal_time(current, next)

    current.move(time, False)
    next.move(time, False)

    nicht_zentraler_stoss(current, next)

    next_collision(current, 1 - time)


def cal_time(current, i):
    time =\
        (
                -math.sqrt(
                        (
                                2*current.v.x*current.x - 2*current.v.x*i.x - 2*i.v.x*current.x + 2*i.v.x*i.x + 2*current.v.y*current.y - 2*current.v.y*i.y - 2*i.v.y*current.y + 2*i.v.y*i.y
                        )**2 - 4*(
                                current.v.x**2 - 2*current.v.x*i.v.x + i.v.x**2 + current.v.y**2 - 2*current.v.y*i.v.y + i.v.y**2
                        )*(
                                current.x**2 - 2*current.x*i.x + i.x**2 + current.y**2 - 2*current.y*i.y + i.y**2 - 4*kugel.RADIUS**2
                        )
                ) - 2*current.v.x*current.x + 2*current.v.x*i.x + 2*i.v.x*current.x - 2*i.v.x*i.x - 2*current.v.y*current.y + 2*current.v.y*i.y + 2*i.v.y*current.y - 2*i.v.y*i.y
        )/(
                2*(
                current.v.x**2 - 2*current.v.x*i.v.x + i.v.x**2 + current.v.y**2 - 2*current.v.y*i.v.y + i.v.y**2
        )
        )
    return time


# Diese Methode ist ueberholt
def collision_kugel(current, balls):
    """
    #reflektiert die Kugeln, die miteinander kollidieren und
    #:param current:
    #:param balls:
    #:return:
    """
    for i in balls:
        # zukuenftige Positionen der Kugeln errechnen --------------------------------------------
        c_x, c_y = current.new_position()
        i_x, i_y = i.new_position()

        # testet, ob die Kugeln im naechsten Schritt kolliediern----------------------------------
        if math.sqrt((c_x - i_x)**2 + (c_y - i_y)**2) <= 2*kugel.RADIUS and (
                i.v != vektor.vektor(0, 0) or current.v != vektor.vektor(0, 0)):

            # Zeit Berechnung der Kollision ------------------------------------------------------
            time =\
                (
                        -math.sqrt(
                                (
                                        2*current.v.x*current.x - 2*current.v.x*i.x - 2*i.v.x*current.x + 2*i.v.x*i.x + 2*current.v.y*current.y - 2*current.v.y*i.y - 2*i.v.y*current.y + 2*i.v.y*i.y
                                )**2 - 4*(
                                        current.v.x**2 - 2*current.v.x*i.v.x + i.v.x**2 + current.v.y**2 - 2*current.v.y*i.v.y + i.v.y**2
                                )*(
                                        current.x**2 - 2*current.x*i.x + i.x**2 + current.y**2 - 2*current.y*i.y + i.y**2 - 4*kugel.RADIUS**2
                                )
                        ) - 2*current.v.x*current.x + 2*current.v.x*i.x + 2*i.v.x*current.x - 2*i.v.x*i.x - 2*current.v.y*current.y + 2*current.v.y*i.y + 2*i.v.y*current.y - 2*i.v.y*i.y
                )/(
                        2*(
                        current.v.x**2 - 2*current.v.x*i.v.x + i.v.x**2 + current.v.y**2 - 2*current.v.y*i.v.y + i.v.y**2
                )
                )

            # Bewegung vor dem Stoss ------------------------------------------------------------- ohne Reibung
            current.move(time, False)
            i.move(time, False)
            # current.x, current.y = current.x + current.v.x*time, current.y + current.v.y*time
            # i.x, i.y = i.x + i.v.x*time, i.y + i.v.y*time

            # Stoss
            # current.v, i.v = zentraler_stoss(current.v, i.v)
            nicht_zentraler_stoss(current, i)

            # Bewegung nach dem Stoss ------------------------------------------------------------ mit Reibung
            current.move(1 - time, True)
            i.move(1 - time, True)
            # current.x, current.y = current.x + current.v.x*(1 - time), current.y + current.v.y*(1 - time)
            # i.x, i.y = i.x + i.v.x*(1 - time), i.y + i.v.y*(1 - time)
        else:
            pass
            # todo normale Bewegung
            """
            Problem: 
            - ausserhalb der Schleife, da pro Kugel nur eine Bewegung statt findet
            - wurde die Kugel schon durch vorherige Kontrollen bewegt?
            - letzte Kugel wird nicht aufgerufen
            """


def zentraler_stoss(v1, v2):
    """
    gibt die Geschwindigkeiten, nach einem zentralen elastischen Stoss zurueck
    :param v1:
    :param v2:
    :return v2, v1: getauschte Geschwindigkeiten
    """
    return v2, v1


def nicht_zentraler_stoss(k1, k2):
    """
    berechnet die Geschwindigkeit nach einem nicht zentralen elastischen Stoss
    :param k1:
    :param k2:
    :return:
    """
    d = vektor.vektor(k2.x - k1.x, k2.y - k1.y)
    norm_d_quadrat = d*d

    v1d = k1.v.x*d.x + k1.v.y*d.y
    v2d = k2.v.x*d.x + k2.v.y*d.y

    k1.v = vektor.vektor(k1.v.x - d.x*(v1d - v2d)/norm_d_quadrat, k1.v.y - d.y*(v1d - v2d)/norm_d_quadrat)
    k2.v = vektor.vektor(k2.v.x - d.x*(v2d - v1d)/norm_d_quadrat, k2.v.y - d.y*(v2d - v1d)/norm_d_quadrat)


def kugeln_stehen_still(k):
    """
    Prueft, ob alle Kugeln still stehen
    :param k:
    :return bool:
    """
    for i in k:
        if i.v.x != 0 or i.v.y != 0:
            return False
    return True


def kugel_zurueck_setzen():
    """
    setzt die weisse Kugel auf die Ursprungsposition zurueck
    :return:
    """
    k[0].eingelocht = False
    k[0].x = X_STR_2
    k[0].y = Y_MID
    dir = 1
    while True:
        if k[0].y >= 0.75 - kugel.RADIUS or k[0].y <= .25 + BORDER + kugel.RADIUS:
            dir *= -1
        if draw.mouse_pressed():
            if not k[0].overlap(k[1:]):
                break
        k[0].y += dir*.001
        tisch()
        draw.show(1)
        draw.clear()


def main():
    """
    Hauptprogram
    - erstellt Fenster und Queue
    - laeuft Spielschleife
    :return:
    """

    draw.set_canvas_size(1000, 1000)
    my_cue = cue.cue()
    kugeln_legen()
    #p[0].ist_am_zug = True
    #current_player = p[0]

    # Spielschleife
    while True:


        tisch()  # Tisch & Kugeln werden gezeichnet
        draw.show(1)



        # Schlagen -------------------------------------------------------------------------------
        if kugeln_stehen_still(k):
                for i in p:
                    print(i.points)
                    print("")
                if p[0].ist_am_zug:
                    p[0].ist_am_zug = False
                    p[1].ist_am_zug = True
                else:
                    p[1].ist_am_zug = False
                    p[0].ist_am_zug = True

                if p[0].ist_am_zug:
                    current_player = p[0]
                else:
                    current_player = p[1]

                print("{} ist am Zug.".format(current_player.name))

                # weisse Kugel setzen
                if k[0].eingelocht:
                    k[0].eingelocht = False
                    k[0].x = X_STR_2
                    k[0].y = Y_MID
                    dir = 1
                    while True:
                        draw.clear()
                        tisch()
                        draw.show(1)
                        if draw.mouse_pressed():
                            if not k[0].overlap(k[1:]):
                                break
                        k[0].y += dir * 0.001
                        if .25 + BORDER + kugel.RADIUS >= k[0].y or k[0].y >= 0.75 - kugel.RADIUS:
                            dir *= -1


                while True:
                    try:
                        winkel = int(input("In welchen Winkel (degrees) wollen sie schlagen"))
                    except:
                        continue
                    my_cue.alpha = math.radians(winkel)
                    draw.clear()
                    tisch()
                    my_cue.draw(k[0])
                    draw.show(1)
                    try:
                        if str(input("Wollen Sie in wirklich in {} schlagen".format(winkel))).lower() == "y":
                            break
                    except:
                        pass
                while True:
                    try:
                        cue_power = float(input("Wie hart wollen sie schlagen [0,2]?"))
                    except:
                        continue
                    if 0 > cue_power or cue_power > 2:
                        print("DEPP!")
                        continue

                    try:
                        if str(input("Wollen Sie in wirklich mit {} power schlagen".format(cue_power))).lower() == "y":
                            # animationn weg
                            while my_cue.pow < 0.5 + 2*cue_power:
                                my_cue.pow += 0.02

                                draw.clear()
                                tisch()
                                my_cue.draw(k[0])
                                draw.show(1)
                            # animation hin
                            while my_cue.pow > 1:
                                my_cue.pow -= 0.2 * cue_power

                                draw.clear()
                                tisch()
                                my_cue.draw(k[0])
                                draw.show(1)

                            k[0].v = my_cue.power(k[0], cue_power)
                            break
                    except:
                        pass

        # Rand Kollision -------------------------------------------------------------------------
        for i in range(len(k)):
            if not k[i].eingelocht:
                if math.hypot(k[i].v.x, k[i].v.y) > 0.00001:
                    collision_border(k[i], current_player)
                else:
                    k[i].v = vektor.vektor(0, 0)

                # Kugeln Kollision -----------------------------------------------------------------------
        for i in range(len(k) - 1):
            if not k[i].eingelocht:
                next_collision(k[i])
                # collision_kugel(k[i], k[i + 1:])

        k[len(k) - 1].move()
        # Bewegen der Kugeln ---------------------------------------------------------------------
        #        for i in k:
        #            if not i.eingelocht:
        #                i.move()

        # draw.show(1)  # zeigt alle Objekte fuer 1 ms
        draw.clear()  # leert die Zeichenflaeche


if __name__ == "__main__":
    print("Herzlich Willkomen zu dem Billard-Simulator 3000")
    main()

