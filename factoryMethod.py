from interface import *


class FactoryMethod:

    def __init__(self, object) -> None:
        
        self.object = object

        self.list = ['Gato', 'Tartaruga', 'Cavalo']
    

    def factory(self):

        if self.object == 'Gato':
            return Gato
        elif self.object == 'Tartaruga':
            return Tartaruga
        elif self.object == 'Cavalo':
            return Cavalo


    def get_tipos_object(self):

        return self.list



Gatoo = FactoryMethod('Cavalo')

g = Gatoo.factory()()

# print(g.me_apresentado())