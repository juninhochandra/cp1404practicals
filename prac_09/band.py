class Band:
    """Musician class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_string = ""
        for musician in self.musicians:
            musician_string += str(musician)
        return f"{self.name} ({musician_string})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        play_string = ""
        for musician in self.musicians:
            play_string += musician.play() + "\n"
        return play_string