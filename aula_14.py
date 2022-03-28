peso = float(input('Digite Seu Peso: '))
altura = float(input('Digite Sua Altura: '))

alt1 = altura ** 2

imc = peso / alt1

if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc < 24.9:
    print('Normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <= 39.9:
    print('Obesidade Leve')
else:
    print('Obesidade Grau II')
