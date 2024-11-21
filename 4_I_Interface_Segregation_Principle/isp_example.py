"""
'   O código abaixo viola o princípio de segregação de interfaces, pois a classe
    Document possui métodos que não são utilizados por todas as suas subclasses.
    Dessa forma, a classe Document deve ser divida em interfaces menores, de modo
    que cada uma delas possua métodos que sejam utilizados por todas as suas subclasses.
"""
from abc import ABC, abstractmethod
class Document(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass

class PDF(Document):
    def load(self):
        print("PDF load method")

    def view(self):
        print("PDF view method")
    
    def format(self):
        print("No use")
    
    def calculate(self):
        print("No use")

document1 = PDF()

# I - Interface Segregation Principle (Princípio da Segregação da Interface):
class DocumentPDF(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentExcel(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
