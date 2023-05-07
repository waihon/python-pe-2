class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

if __name__ == "__main__":
    sun = Star("Sun", "Milky Way")
    print(sun) # <__main__.Star object at 0x7f038befe310>
