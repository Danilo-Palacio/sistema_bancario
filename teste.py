from abc import ABC, abstractmethod

class Historico:
    def __init__(self):
        self.adicionar_transacao() #transacao:Transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self):
        pass

class Saque(Transacao):
    def registrar(self):
        return("Registrou o Saque")

class Deposito(Transacao):
    def registrar(self):
        return("Registrou o Deposito")



