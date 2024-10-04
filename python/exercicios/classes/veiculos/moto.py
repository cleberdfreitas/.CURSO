from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, tipo):
        super().__init__(marca, modelo, cor)
        self._tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Cor: {self._cor} - Tipo: {self._tipo} - Status: {status}"
    
    # Método ligar na classe Moto: Vi que a classe Moto não implementa o método ligar, que é abstrato na classe Veiculo. 
    # Como Veiculo é uma classe abstrata, todas as subclasses precisam implementar os métodos abstratos. Então, seria interessante adicionar o método ligar na classe Moto também. Por exemplo:
    # Status do veículo: Atualmente, o status "ligado" ou "desligado" é sempre "desligado" 
    # porque a variável _ligado nunca é alterada. Você poderia adicionar lógica no método ligar para mudar o status do veículo. Por exemplo, dentro do método ligar:
    
    def ligar(self):
        self._ligado = True
        print("A moto {self._modelo} está ligada.")