vet = []
i = 0
soma = 0
apr = 0
rec = 0
while True:
    i = i + 1
    nota = float(input(f'Digite a nota {i}: '))
    while nota > 10 or nota < 0:
        print("\nValor invalido\n")
        nota = float(input(f'\nDigite a nota {i}:   '))
    vet.append(nota)
    op = int(input("\nDeseja continuar? 1- Sim 2-Nao\n"))
    while op != 1 and op != 2:
        op = int(input("\nInvalido\n"))
    if op == 2:
        maior, segmaior = vet[0], vet[0]
        for n in range(len(vet)):
            if vet[n] > maior:
                maior = vet[n]
            elif vet[n] > segmaior:
                segmaior = vet[n]
            soma = soma + vet[n]
            if vet[n] >= 8:
                apr = apr + 1
            if vet[n] >= 4 and vet[n] < 7:
                rec = rec + 1

        print(f"Foram lidas {i} notas")
        print(f"A media foi de {soma / len(vet):.2f} pontos")  # Correção aqui
        print(f"A maior nota é: {maior}")
        print(f"A segunda maior nota é: {segmaior}")
        print(f"Foram aprovados {apr} alunos, isso representa {(apr / i) * 100:.2f}%")
        print(f"{rec} alunos ficaram de recuperacao,  isso representa {(rec / i) * 100:.2f}%")

        break
