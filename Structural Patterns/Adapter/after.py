import math


class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def fits(self, peg):
        return self.radius >= peg.radius


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg):
        self.peg = peg
        self.radius = self.get_radius()

    def get_radius(self):
        self.radius = self.peg.get_width() * math.sqrt(2) / 2
        return self.radius


def main():
    # Create a round hole of radius 5
    hole = RoundHole(5)
    # Create a round peg of radius 5
    rpeg = RoundPeg(5)
    # Check if the peg fits the hole
    print("Hole fits Round peg? ", hole.fits(rpeg))
    # Create a square peg of width 5
    small_sqpeg = SquarePeg(5)
    # check if the peg fits the hole
    try:
        print("Hole fits Square peg? ", hole.fits(small_sqpeg))
    except AttributeError:
        print("Hole does not fit square pegs")
    # Create a square peg adapter
    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    # Check if the square peg fits the hole
    print("Hole fits Square peg? ", hole.fits(small_sqpeg_adapter))


if __name__ == "__main__":
    main()