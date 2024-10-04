class Livro:
    Livros = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicado = ano_publicado
        self._disponivel = True
        Livro.Livros.append(self)
            
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            
    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado} | {'Disponível' if self._disponivel else 'Indisponível'}'
   
    @staticmethod
    def verificar_disponibilidade(ano):
        return [str(livro) for livro in Livro.Livros if livro._ano_publicado == ano]