"""
    O código abaixo viola o princípio aberto/fechado, pois a classe Company
    possui um método que realiza diferentes tarefas de acordo com o valor
    passado como argumento, o que pode ser um problema caso a classe seja
    modificada no futuro.
"""
class Company:
    def do_work(self, worker: int) -> None:
        if worker == 1:
            print("Programmer creating code")
        elif worker == 2:
            print("Seller selling the product")
        elif worker == 3:
            print("Human Resources hiring new devs")
        elif worker == 4:
            print("Frontend raising bugs for production")
        else:
            print("Error, no Worker!")

company = Company()
company.do_work(4)

# O - Open/Closed Principle (Princípio Aberto/Fechado):
class Programmer: # Criando extensão
    def make(self) -> None: # Método aberto para extensão
        print("Programmer creating code")

class Seller: # Criando extensão
    def make(self) -> None: # Método aberto para extensão
        print("Seller selling the product")

class HumanResources: # Criando extensão
    def make(self) -> None: # Método aberto para extensão
        print("Human Resources hiring new devs")

class Company:
    def do_work(self, worker: any) -> None: # Método fechado para modificação mas aberto para extensão
        worker.make()

programmer = Programmer()
seller = Seller()
human_resources = HumanResources()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(human_resources)