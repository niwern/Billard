class player(object):
    def __init__(self, name="Pascal"):
        self.points = 0
        self.name = name
        self.ist_am_zug = False
        self.marker = None

    def get_point(self):
        self.points += 1

    def set_marker(self, marker):
        self.marker = marker
        print("{} hat die Kugeln {} Marker".format(self.name, self.marker))
