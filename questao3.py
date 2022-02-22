# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
# desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no
# cálculo da média;
import json


def analyse_data(array: list) -> dict:
    biggest = 0
    smallest = 0
    array_sum = 0
    counter = 0
    for num in array:
        if num != 0:
            array_sum += num
            counter += 1
    average = array_sum / counter
    above_average = 0

    for i in range(len(array)):
        if array[i] == 0:  # Makes 0 be disconsidered of array
            continue
        if array[i] > average:
            above_average += 1
        if i == 0:
            biggest = array[i]
            smallest = array[i]
        else:
            if array[i] < smallest:
                smallest = array[i]
            elif array[i] > biggest:
                biggest = array[i]

    dados_faturamento_mes = dict()

    dados_faturamento_mes['menor'] = smallest
    dados_faturamento_mes['maior'] = biggest
    dados_faturamento_mes['acima_media'] = above_average

    return dados_faturamento_mes


def put_json_in_file(dictionary):
    json_object = json.dumps(dictionary, indent=4)
    f = open("faturamento_diario.json", "w")
    f.write(json_object)
    f.close()


def main():
    array = [5, 9, 1, 6, 0, 7, 0, 0, 5, 3, 7, 11, 5, 1, 0, 9, 4]  # in thousands
    dados_faturamento_mes = analyse_data(array)
    put_json_in_file(dados_faturamento_mes)
    print(f'''
Menor faturamento do mês: {dados_faturamento_mes['menor']}
Maior faturamento do mês: {dados_faturamento_mes['maior']}
Qtd dias que o faturamento passou a média mensal: {dados_faturamento_mes['acima_media']}
    ''')


main()
