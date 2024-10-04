'''Listas (mutáveis)
As listas são ideais quando você precisa de uma coleção de elementos que pode ser modificada ao longo do tempo. 
Por exemplo, ao criar uma lista de tarefas que pode ser atualizada com novos itens ou marcada como concluída.'''

# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

'''Tuplas (Imutáveis)
Já as tuplas são apropriadas quando se deseja garantir que os elementos não sejam alterados após a criação. 
Isso é útil para dados que devem permanecer constantes ao longo do tempo. 
Como as tuplas são imutáveis, elas podem ter um desempenho ligeiramente melhor em operações de leitura e acesso a elementos. 
Isso também as tornam adequadas para situações em que a eficiência é crucial.'''

# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])