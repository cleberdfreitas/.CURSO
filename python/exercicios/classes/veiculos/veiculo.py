from abc import ABC, abstractmethod # Importa as classes ABC (Abstract Base Class) e o decorador @abstractmethod do módulo abc, 
                                    # que são essenciais para criar classes abstratas.

class Veiculo:
    def __init__(self, marca, modelo, cor):
        self._marca = marca
        self._modelo = modelo    
        self._cor = cor    
        self._ligado = False
    
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self._modelo} - Cor: {self._cor} - Status: {status}"
    
    @abstractmethod
    def ligar(self):
        pass

'''
exemplo de classe abstrata

class Livro(MaterialBiblioteca):
    def __init__(self, titulo, autor, data_publicacao, isbn):
        super().__init__(titulo, autor, data_publicacao)
        self._isbn = isbn

    def emprestar(self):
        # Lógica específica para emprestar um livro
        print(f"Livro '{self._titulo}' emprestado.")

    def devolver(self):
        # Lógica específica para devolver um livro
        print(f"Livro '{self._titulo}' devolvido.")

class DVD(MaterialBiblioteca):
    def __init__(self, titulo, autor, data_publicacao, duracao):
        super().__init__(titulo, autor, data_publicacao)
        self._duracao = duracao

    def emprestar(self):
        # Lógica específica para emprestar um DVD
        print(f"DVD '{self._titulo}' emprestado.")

    def devolver(self):
        # Lógica específica para devolver um DVD
        print(f"DVD '{self._titulo}' devolvido.")'''