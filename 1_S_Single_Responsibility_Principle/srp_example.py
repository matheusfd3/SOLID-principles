"""
    O código abaixo viola o princípio da responsabilidade única, pois a classe 
    Process é responsável por realizar a validação dos dados de entrada e também 
    por realizar a conexão com o banco de dados.
"""
class Process:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str): # 1ª responsabilidade
            print("Acessando o banco de dados...") # 2ª responsabilidade
            print("Verificando existência do usuário...")
            print("Cadastro de usuário realizado com sucesso!") # 3ª responsabilidade
        else:
            raise Exception("Dados inválidos")

# S - Single Responsibility Principle (Princípio da Responsabilidade Única):
class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_user_exists(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_exception("Dados inválidos")
    
    def __verify_input_data(self, username: str, password: str) -> bool:
        if isinstance(username, str) and isinstance(password, str):
            return True
        return False
    
    def __verify_user_exists(self, username: str) -> None:
        print("Acessando o banco de dados...")
        print("Verificando existência do usuário...")

    def __insert_new_user(self, username: str, password: str) -> None:
        print("Cadastro de usuário realizado com sucesso!")
    
    def __raise_exception(self, message: str) -> None:
        raise Exception(message)