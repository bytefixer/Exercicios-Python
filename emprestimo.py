'''
    Enunciado: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.
'''
import time


try:
    valor_casa = float(input('Digite o valor da casa: '))
    salario = float(input('Informe seu salário: '))
    anos = int(input('Anos a pagar: '))

except ValueError:
    time.sleep((1.5))
    print("Por favor, insira valores numéricos.")
    exit()

meses = anos * 12
parcelas = valor_casa / meses
minimo = (salario / 100) * 30

print(f'\nO valor da casa, dividido em {meses} meses, é de: R${parcelas:.2f} por mês.\n')

print("...Calculando empréstimo bancário...")
time.sleep(2.3)

if(parcelas < minimo):
    print('\nSeu emprestimo foi aprovado!')
else:
    print(f'\nSeu empréstimo não foi aprovado.\n'
          f'O valor das parcelas é maior que 30% do seu salário que é de R${minimo}.')