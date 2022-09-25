from abc import ABC, abstractproperty


class Fees(ABC):
    @abstractproperty
    def classname(self):
        pass


class Class10(Fees):
    # @property
    def classname(self):
        print("I am in class 10")

# c=Class10()
# c.classname
Class10().classname
