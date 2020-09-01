# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        self.name = name
        self.info = [name, lat, lon]
        super().__init__(lat, lon)

    def __repr__(self):
        return " ".join([str(i) for i in self.info])



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        self.difficulty = difficulty
        self.size = size
        super().__init__(lat, lon, name)
        self.info = [name, difficulty, size, lat, lon]


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(name='Catacombs', lat=41.70505, lon=-121.51521)

# YOUR CODE HERE)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(name="Newberry Views", difficulty=1.5, size=2, lat=44.052137, lon=-121.41556)

# Print it--also make this print more nicely
print(geocache)
