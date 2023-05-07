class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

if __name__ == "__main__":
    for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
        for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
            # Each class is considered to be a subclass of itself.
            print(issubclass(cls1, cls2), end="\t")
        print()
        """
        True  False   False
        True  True    False
        True  True    True
        """
