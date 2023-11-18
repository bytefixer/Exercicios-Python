nome = input('Digite o nome do(a) aluno(a): ')
nome_cap = nome.capitalize()

def calcular_media(notas):
    if not notas:
        return None
    soma = sum(notas)
    media = soma / len(notas)
    return media

def inserir_notas():
    notas = []
    for i in range(5):
        while(True):
            try:
                inserir = float(input("Digite uma nota: "))
                notas.append(inserir)
                break
            except ValueError:
                print("Por favor, digite um número válido.")
    return notas

notas_aluno = inserir_notas()
resultado_calculo = calcular_media(notas_aluno)

if resultado_calculo is not None:
    print(f"\nA média das notas de {nome_cap} é: {resultado_calculo:.1f}")
