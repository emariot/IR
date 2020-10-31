
salario = input('Digite seu salário brut: R$')
salario = float(salario)

def calculo():

    faixas = {
        0:0.0,
        1:7.5,
        2:15,
        3:22.5,
        4:27.5
        }
    deducoes = {
        0:0.0,
        1:142.80,
        2:354.80,
        3:636.13,
        4:869.36
        }

    if (salario <= 1903.98):
        faixa = 0
    elif (salario > 1903.98)and(salario <= 2826.65):
        faixa = 1
    elif (salario > 2826.65)and(salario <= 3751.05):
        faixa = 2
    elif (salario > 3751.05)and(salario <= 4664.68):
        faixa = 3
    else:
        faixa = 4

    imposto = salario * (faixas[faixa]/100)
    deducao = deducoes[faixa]
    pagar = abs(imposto - deducao)
    liquido = salario - pagar
    
    m1 = "Bruto: %10.2f, Faixa: %d, Imposto: %5.2f" %(salario, faixa, imposto)
    m2= 'ValorPadrão: %5.2f, Pagar: %5.2f, Líquido: %5.2f'%(deducao, pagar, liquido)
    
    print(m1)
    print(m2)


if __name__ == '__main__':
    calculo()
