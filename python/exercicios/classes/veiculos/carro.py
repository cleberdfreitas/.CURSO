from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, portas):
        super().__init__(marca, modelo, cor)
        self._portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Cor: {self._cor} - Portas: {self._portas} - Status: {status}"
    
    def ligar(self):
        self._ligado = True
        print(f"O carro {self._modelo} está ligado.")