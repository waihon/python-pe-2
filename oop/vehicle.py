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

    my_vehicle = Vehicle()
    my_land_vehicle = LandVehicle()
    my_tracked_vehicle = TrackedVehicle()
    
    for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
        for cls in [Vehicle, LandVehicle, TrackedVehicle]:
            print(isinstance(obj, cls), end="\t")
        print()
    """
    True    False   False
    True    True    False
    True    True    True
    """
