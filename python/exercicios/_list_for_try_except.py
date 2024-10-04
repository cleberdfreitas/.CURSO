#range(start, stop, step)

l_nume = [1,2,3,4,5,6,7,8,9,10]
l_nome = ['Ana','Marco','João','Bia']
l_anos = [1984, 2024]

'''for elemento in l_nume:
    print(f'-> {elemento}\n')'''

# - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
'''soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)'''
# O segundo argumento de da função range é exclusivo, então range(1, 11) 
# inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range). 
# Isso garante que apenas números ímpares sejam considerados.

# Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:
'''for i in range(10,0,-1):
    print(f'{i} ')'''

'''numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")'''


# soma dos elementos de uma lista com for e usar try except para validar
'''lista_numeros = ['a', 5, 8, 3, 7]
soma = 0
try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")'''
# Exception é uma classe base para todas as exceções em Python. Capturar Exception 
# permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. O "as e" é opcional, 
# mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.

# código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia
'''lista_valores = [15, 20, 25, 30]
soma_valores = 0
try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")'''
# ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. 
# Este bloco except é destinado a lidar especificamente com esse tipo de erro.