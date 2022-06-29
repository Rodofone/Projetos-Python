import matplotlib.pyplot as plt

while True:
    smplx = list()
    restr = list()
    colIN = colOUT = index1 = index2 = fim = 0
    LP = list()
    NLP = list()
    count = 1
    repetir = 0
    lista_rest = list()
    x1 = False
    x2 = False
    print('\n')
    print('--'*50)
    print('A operação será feita pelo método Simplex ou método Gráfico?')
    print('[ 1 ] - Método Gráfico (Apenas Duas variáveis): ')
    print('[ 2 ] - Método Simplex (Apenas maximização): ')
    graf_simpl = int(input('Opção: '))
    while graf_simpl < 1 or graf_simpl > 2:
        print('Opção inválida!')
        print('A operação será feita pelo método Simplex ou método Gráfico?')
        print('[ 1 ] - Método Gráfico (Apenas Duas variáveis): ')
        print('[ 2 ] - Método Simplex (Apenas maximização): ')
        graf_simpl = int(input('Opção: '))

    print('----------------------- Variáveis ------------------------')
    if graf_simpl == 1:
        qtd_var = int(input("O cálculo tem quantas variáveis? (Minímo 2 e Máximo 2): "))
        while qtd_var != 2:
            print("Digite um valor válido")
            qtd_var = int(input("O cálculo tem quantas variáveis? (Mínimo 2 e Máximo 2): "))
    if graf_simpl == 2:
        qtd_var = int(input("O cálculo tem quantas variáveis? (Minímo 2 e Máximo 6): "))
        while qtd_var < 2 or qtd_var > 6:
            print("Digite um valor válido")
            qtd_var = int(input("O cálculo tem quantas variáveis? (Mínimo 2 e Máximo 6): "))
    print('----------------------- Restrições ------------------------')
    qtd_rest = (int(input("Quantas restrições tem este cálculo? ")))

    print('----------------------- FOMax(Z) ------------------------')

    if graf_simpl == 1:
        for i in range(qtd_var):
            if i+1 == 1:
                x1 = float(input(f"Digite o valor de x{i+1}: "))
            if i+1 == 2:
                x2 = float(input(f"Digite o valor de x{i+1}: "))

    elif graf_simpl == 2:
        restr.append(1)
        for i in range(qtd_var):
            x1 = int(input(f"Digite o valor de x{i+1}: "))
            restr.append(x1*-1)
        for i in range(qtd_rest):
            restr.append(0)
        restr.append(0)
        smplx.append(restr)
        print(f'FOMAX: {restr}')
        print(qtd_var)
        restr = list()
    print('----------------------- Restrições ------------------------')
    if graf_simpl == 1:
        for i in range(qtd_rest):
            if qtd_var == 2:
                print(f'-------- Restrição{i+1} --------')
                restx1 = float(input("Digite a quantidade de x1: "))
                lista_rest.append(restx1)
                restx2 = float(input("Digite a quantidade de x2: "))
                lista_rest.append(restx2)
                operador = str(input("Digite o operador da restrição (No Máximo(<=): ").strip())
                while True:
                    if operador == '<=':
                        break
                    operador = str(input("Digite o operador da restrição (No Máximo(<=): ").strip())
                lista_rest.append(operador)
                rest = int(input("Digite a quantidade máxima ou miníma: "))
                lista_rest.append(rest)
                print(f'Restrição{i+1}: {restx1}.x1 + {restx2}.x2 {operador} {rest}')

    if graf_simpl == 2:
        for i in range(qtd_rest):
            print(f'-------- Restrição{i+1} --------')
            restr.append(0)
            for v in range(qtd_var):
                r1 = int(input(f"Digite a quantidade de x{v+1}: "))
                restr.append(r1)
            operador = str(input("Digite o operador da restrição (No Máximo(<=): ").strip())
            while True:
                if operador == '<=':
                    break
                operador = str(input("Digite o operador da restrição (No Máximo(<=): ").strip())
            for r in range(qtd_rest):
                if r == i:
                    restr.append(1)
                else:
                    restr.append(0)
            limite = int(input("Digite a quantidade máxima ou miníma: "))
            restr.append(limite)
            print(f'Restrição [{i}]: {restr}')
            smplx.append(restr)
            restr = list()
        qtd_var = qtd_rest + qtd_var + 2

    if graf_simpl == 1:
        print('----------------------- Gráfico ------------------------')
        # Definir Região
        i = 0
        r = 4
        while qtd_rest + 1 > i + 1:
            i += 1
            if i == 1:
                a = lista_rest[3] / lista_rest[0]
                b = lista_rest[3] / lista_rest[1]
                defx = [0, a]
                defy = [b, 0]
                plt.plot(defx, defy, label=f"R{i}")
            else:
                a = lista_rest[3 + (r - 4)] / lista_rest[0 + (r - 4)]
                b = lista_rest[3 + (r - 4)] / lista_rest[1 + (r - 4)]
                defx = [0, a]
                defy = [b, 0]
                plt.plot(defx, defy, label=f"R{i}")
            r += 4
        # Teste de Região
        tdr = int(input("Informe o valor de teste de região: "))
        testregx = [tdr, tdr, tdr, 0]
        testregy = [tdr, 0, tdr, tdr]
        plt.plot(testregx, testregy, label="Teste de Região")
        # Teste FOMax(Z1 = ..., Z2 = ...)
        z1 = int(input("Informe o valor de Z1: "))
        z2 = int(input("Informe o valor de Z2: "))
        e = z1 / x1
        f = z1 / x2
        g = z2 / x1
        h = z2 / x2
        testFOx = [e, 0]
        testFOy = [0, f]
        plt.plot(testFOx, testFOy, label=f"Z1={z1}")
        testFOx = [g, 0]
        testFOy = [0, h]
        plt.plot(testFOx, testFOy, label=f"Z2={z2}")
        # Gráfico Finalizado
        plt.legend()
        plt.show()
    # *********************************************** Simplex ***********************************************
    elif graf_simpl == 2:
        for repetir in range(10):
            # Desenhar Tabela
            if count == 1:
                smplxConta = smplx.copy()
                print('--'*15 + f'Tabela {count}' + '--'*15)
                for l in range(0, qtd_rest+1):
                    for c in range(0, qtd_var):
                        print(f'|{smplx[l][c]:^7.2f}', end='')
                    print()
            # Encontrar coluna IN
            for l in range(0, qtd_rest+1):
                for c in range(0, qtd_var):
                    if colIN == 0 or colIN < 0:
                        for i in range(c):
                            if smplx[0][c] < 0:
                                teste = colIN
                                if teste * -1 < smplx[0][c] * -1:
                                    colIN = smplx[0][c]
                                    index1 = c
            # Encontrar coluna OUT
            if colIN < 0:
                for l in range(0, qtd_rest+1):
                    for c in range(0, qtd_var):
                        if l >= 1:
                            if smplx[l][index1] != 0:
                                if colOUT == 0:
                                    colOUT = smplx[l][qtd_var - 1] / smplx[l][index1]
                                    index2 = l
                                if colOUT > smplx[l][qtd_var - 1] / smplx[l][index1]:
                                    colOUT = smplx[l][qtd_var - 1] / smplx[l][index1]
                                    index2 = l
            # Calcular LP e NLP
            for l in range(0, qtd_rest+1):
                for c in range(0, qtd_var):
                    if l == index2:
                        if smplx[index2][c] != 0:
                            LP.append(smplx[index2][c] / smplx[index2][index1])
                        else:
                            LP.append(0)
            NLP = LP.copy()
            LP = list()

            # Atualizar linha com novos valores
            for l in range(0, qtd_rest+1):
                for c in range(0, qtd_var):
                    if l != index2:
                        if c <= 1:
                            mult = smplx[l][index1] * -1
                        novo_valor = smplx[l][c] + NLP[c] * mult
                        smplxConta[l][c] = novo_valor
                    else:
                        smplxConta[index2][c] = NLP[c]

            # Desenhar Tabela
            count += 1
            print('--'*15 + f'Tabela {count}' + '--'*15)
            for l in range(0, qtd_rest+1):
                for c in range(0, qtd_var):
                    print(f'|{smplxConta[l][c]:^7.2f}', end='')
                print()

            # Reiniciar conta
            fim = 0
            for l in range(0, qtd_rest + 1):
                for c in range(0, qtd_var):
                    if l == 0:
                        if smplxConta[0][c] < 0:
                            colIN = colOUT = index1 = index2 = teste = novo_valor = 0
                            LP = list()
                            NLP = list()
                            smplx = smplxConta.copy()
                        elif smplx[0][c] >= 0:
                            fim += 1
                            if fim == qtd_var:
                                print(f"Lucro máximo de R${smplx[0][qtd_var - 1]:.2f}")
                                exit()
    lista_rest = []

