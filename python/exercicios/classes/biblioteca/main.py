'''
Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, 
autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro 
e retorna uma lista dos livros disponíveis publicados nesse ano.

Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou 
não após o empréstimo.

No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros 
disponíveis publicados em um ano específico.

Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe 
Livro e exiba a mensagem formatada utilizando o método str.

'''
from livro import Livro

livro_mochileiro = Livro('O guia do Mochileiro das Galáxias', 'Douglas Adams', 1979)
livro_calculava = Livro('O homem que calculava', 'Malba Tahan', 1938)
livro_calculava.emprestar() ## Utilizei somente pra testar

print(livro_calculava)
print(livro_mochileiro)