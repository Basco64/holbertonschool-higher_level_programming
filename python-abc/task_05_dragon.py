#!/usr/bin/python3


class SwimMixin:
    """swimmixin class"""

    def swim(self):
        """print swim"""
        print("The creature swims!")


class FlyMixin:
    """flymixin class"""

    def fly(self):
        """print fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""

    def roar(self):
        """print roar"""
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
