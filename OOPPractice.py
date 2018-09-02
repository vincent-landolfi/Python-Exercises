class Dog():
    "A class to represent a good boy... yes he is..."
    
    def __init__(self,name):
        '''(Dog,str) -> NoneType
        Create a new dog named name
        '''
        self._name = name
        
    def give_toy(self,new_toy):
            '''(Dog,Toy) -> NoneType
            Give this dog new_toy to play with, replacing any
            old toys it may have had
            '''
            self._toy = new_toy    
            
    def play(self):
        '''(Dog) -> NoneType
        Let the dog plau with its toy
        '''
        for i in range(100):
            self._toy.squeeze()
        
class Toy():
    '''A class to represent a dog toy'''
    
    def __init__(self,sound):
        '''(toy,str) -> NoneType
        Create a new toy that will print sound when played with
        '''
        self._sound = sound
        
    def squeeze(self):
        '''(Toy) -> NoneType
        Make a sound
        '''
        print(self._sound)
    
        
        
if(__name__ == "__main__"):
    toy1 = Toy('squeek')
    toy1.squeeze()
    dog1 = Dog("Rover")
    dog1.give_toy(toy1)
    dog1.play()