# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.
#
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente
# definido no código;

fibonacci_numbers = [0]
previous = 0
current = 1
precision = 100
# (Last element in 100 precision: 354224848179261915075)

for i in range(precision):
    fibonacci_numbers.append(current)
    auxiliary = current
    current += previous
    previous = auxiliary

num = int(input('Digite um número para descobrir se ele se encontra na sequência de Fibonacci: '))
print('Está em Fibonacci' if num in fibonacci_numbers else 'Não está em Fibonacci')
