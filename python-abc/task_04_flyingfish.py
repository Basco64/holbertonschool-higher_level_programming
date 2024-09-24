#!/usr/bin/python3


class Fish:
    """Fish class"""

    def swim(self):
        """print swim"""
        print("The fish is swimming")

    def habitat(self):
        """prints habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """print fly"""
        print("The bird is flying")

    def habitat(self):
        """print habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """flyingfish class"""

    def fly(self):
        """print fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """print swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """print habitat"""
        print("The flying fish lives both in water and the sky!")


flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
print(FlyingFish.mro())
