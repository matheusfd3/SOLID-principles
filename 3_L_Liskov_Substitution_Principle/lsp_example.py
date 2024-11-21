"""
    O código abaixo viola o princípio de substituição de Liskov, pois a classe
    Felino sobrescreve o método comer da classe Animal, o que faz com que o
    comportamento do método seja diferente do esperado.
"""
class Animal:
    def comer(self):
        print("O Animal está comendo")
    
    def andar(self):
        print("O Animal está andando ma jaula")

class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")
    
    def comer(self):
        print("O Felino está comendo")

class Leao(Felino):
    def rugir(self):
        print("O Leão está rugindo alto!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

renato = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

renato.observa(animal)

# L - Liskov Substitution Principle (Princípio da Substituição de Liskov):
class Animal:
    def comer(self):
        print("O Animal está comendo")
    
    def andar(self):
        print("O Animal está andando ma jaula")

class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")

class Leao(Felino):
    def rugir(self):
        print("O Leão está rugindo alto!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

renato = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

renato.observa(animal)