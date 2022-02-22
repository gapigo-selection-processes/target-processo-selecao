# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no
# código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Two lines answer
string = input('Insira a string a ser invertida: ').strip()
print(f'Resposta: {string[::-1]}')

# Full code answer
string = input('Insira a string a ser invertida: ').strip()
answer = ''
for index in range(len(string)-1, -1, -1):
    answer += string[index]
print(f'Resposta: {answer}')