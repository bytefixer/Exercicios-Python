import time


def banco_questoes(qtd):
    print(f"Digite as respostas das {qtd} questões. Alternativas disponíveis: A, B, C, D.")
    time.sleep(2)

def ler_resp(questao):
    while True:
        resposta = input(f"Digite a resposta da questão {questao}: ")
        if resposta.isalpha() and len(resposta) == 1:
            return resposta.upper()
        else:
            print("ATENÇÃO! Digite apenas um caractere válido.\n")

qtd = 5
pont = 0

banco_questoes(qtd)

for i in range(1, qtd + 1):
    resposta = ler_resp(i)

    if i == 1 and resposta == 'B':
        pont += 1
    elif i == 2 and resposta == 'A':
        pont += 1
    elif i == 3 and resposta == 'D':
        pont += 1
    elif i == 4 and resposta == 'C':
        pont += 1
    elif i == 5 and resposta == 'B':
        pont += 1

percent = (pont / qtd) * 100

print(f"\nA quantidade de acertos é: {pont}")
print(f"Sua % de acertos é de: {percent:.0f}%")

if(pont >= 3):
    print("\nParabéns! :)")
else:
    print("\nNão desanime. Continue os estudos! =)")

