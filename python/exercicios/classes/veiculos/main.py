'''
1 - Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. 
    A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

2 - Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, 
    modelo e o estado de ligado/desligado do veículo.

3 - Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, 
    inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

4 - Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da 
    classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

5 - Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo 
    chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

6 - Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o 
    método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.

7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de 
    Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
'''
# 1- Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# 2- No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
# 3- Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4- No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
# 5- Em um arquivo chamado main.py, importe a classe Carro.
# 6- No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

import os
os.system('cls')

from carro import Carro
from moto import Moto

carro = Carro('Wolks', 'Gol', 'Preto', 2)
moto = Moto('Honda', 'CG', 'Cinza', 'casual')

print(carro)
print(moto)

carro.ligar()
moto.ligar()

