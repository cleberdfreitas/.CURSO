from exercicios import Livro

livro_dracula = Livro('Dracula', 'Bram Stoker', 1897)
livro_cthulhu = Livro('Chamado de Cthulhu', 'H.P. Lovecraft', 1928)
livro_retrato_Dorian = Livro('O Retrato de Dorian Gray', 'Oscar Wilde', 1890)


print(Livro.verificar_disponibilidade(1897)) ##O uso duplicado desse print é para teste se o emprestar funciona corretamente
livro_dracula.emprestar()
print(Livro.verificar_disponibilidade(1897))