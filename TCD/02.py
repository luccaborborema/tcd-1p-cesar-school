def ler_arquivo(arq):
    abrir = open(arq, 'r', encoding='utf8')
    copia = abrir.readlines()
    abrir.close()
    return copia

def listar(arq):
    abrir = open(arq, 'r', encoding='utf8')
    copia = abrir.readlines()
    for linha in range(0, len(copia)):
        print(copia[linha])
        abrir.close()

def vendas():
    global valor_total
    global nome_completo
    global medicamento
    global quantidade
    global valor_t
    global pagamento
    global cpf
    global i
    global arq
    global clientes
    print('DATA DA COMPRA')
    data = input('DATA DE COMPRA DD-MM-YYY (EX: 11-22-3333): ')
    print('MATRÍCULA DOS FUNCIONÁRIOS: ')
    funcionarios = open('funcionarios.txt', 'r', encoding='utf8')
    for linha in funcionarios:
        if 'MATRÍCULA: ' in linha:
            print(linha.strip())
    try:
        matricula = int(input('DIGITE A MATRÍCULA DO FUNCIONÁRIO QUE REALIZARÁ A VENDA: '))
    except ValueError:
        print("MATRICULA INVALIDA! TENTE NOVAMENTE!")
        matricula = int(input('DIGITE A MATRÍCULA DO FUNCIONÁRIO QUE REALIZARÁ A VENDA: '))
    try:
        cpf = int(input('DIGITE O CPF DO CLIENTE: '))
        clientes = open('clientes.txt', 'r', encoding='utf8')
        arq = ler_arquivo('clientes.txt')
        i = arq.index('CPF: ' + str(cpf) + '\n')
    except ValueError:
        print("CPF INVALIDO! TENTE NOVAMENTE!")
        cpf = int(input('DIGITE O CPF DO CLIENTE: '))
        clientes = open('clientes.txt', 'r', encoding='utf8')
        arq = ler_arquivo('clientes.txt')
        i = arq.index('CPF: ' + str(cpf) + '\n')
    for a in range(0, 2):
        print(arq[i + a])
    clientes.close()
    cont = ''
    valor_total = 0
    while cont != '-1':
        try:
            medicamento = input('DIGITE O NOME DO MEDICAMENTO: ')
            medicamentos = open('clientes.txt', 'r', encoding='utf8')
            arq = ler_arquivo('medicamentos.txt')
            i = arq.index('NOME: ' + medicamento + '\n')
        except ValueError:
            print("MEDICAMENTO INVALIDO! TENTE NOVAMENTE!")
            medicamento = input('DIGITE O NOME DO MEDICAMENTO: ')
            medicamentos = open('clientes.txt', 'r', encoding='utf8')
            arq = ler_arquivo('medicamentos.txt')
            i = arq.index('NOME: ' + medicamento + '\n')
        for a in range(0, 1):
            print(arq[i + a])
            for a in range(0, 5):
                print(arq[i + a])
        try:
            quantidade = int(input('DIGITE A QUANTIDADE QUE DESEJA: '))
        except ValueError:
            print("QUANTIDADE INVALIDA")
            quantidade = int(input('DIGITE A QUANTIDADE QUE DESEJA: '))
        arq = ler_arquivo('medicamentos.txt')
        for linha in range(4, 5):
            med = arq[i+linha].split()
            quant = med[1]
            nova_quantidade = int(quant) - quantidade
            arq[i + 4] = 'QUANTIDADE: ' + str(nova_quantidade) + '\n'
            arq2 = open("medicamentos.txt", 'w', encoding='utf8')
            # quantidade = str(quantidade) + ", "
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            medicamentos = open('clientes.txt', 'r', encoding='utf8')
            arq = ler_arquivo('medicamentos.txt')
            i = arq.index('NOME: ' + medicamento + '\n')
            for a in range(0, 1):
                for a in range(2, 3):
                    val = arq[i + a].split()
                    valor = float(val[1])
                    valor1 = valor
                    valor_t = valor * quantidade
                    valor_total += valor_t
        cont = (input('DESEJA VENDER OUTRO PRODUTO? PRESSIONE ENTER PARA CONTINUAR OU -1 PARA PROSSEGUIR: '))
        if cont == '-1':
            print('VALOR TOTAL: ', valor_total)
            try:
                pagamento = int(input('1 - À VISTA\n2- DÉBITO\n3 - CRÉDITO\nDIGITE A FORMA DE PAGAMENTO: '))
                if pagamento == 1:
                    pagamento = 'Á VISTA'
                elif pagamento == 2:
                    pagamento = 'DÉBITO'
                elif pagamento == 3:
                    pagamento = 'CRÉDITO'
            except ValueError:
                print("METODO SELECIONADO INVALIDO")
                pagamento = int(input('1 - À VISTA\n2- DÉBITO\n3 - CRÉDITO\nDIGITE A FORMA DE PAGAMENTO: '))
                if pagamento == 1:
                    pagamento = 'Á VISTA'
                elif pagamento == 2:
                    pagamento = 'DÉBITO'
                elif pagamento == 3:
                    pagamento = 'CRÉDITO'
    clientes = open('clientes.txt', 'r', encoding='utf8')
    arq = ler_arquivo('clientes.txt')
    i = arq.index('CPF: ' + str(cpf) + '\n')
    for a in range(1, 2):
        nome = arq[i + a].split()
        nome_completo = nome[1]
    nota_individual = open(nome_completo + '_' + data + '.txt', 'w', encoding='utf8')
    nota_individual.write('DATA DA COMPRA: ' + str(data) + '\n')
    nota_individual.write('VENDEDOR: ' + str(matricula) + '\n')
    nota_individual.write('CPF DO CLIENTE: ' + str(cpf) + '\n')
    nota_individual.write('NOME DO CLIENTE: ' + nome_completo + '\n')
    nota_individual.write('MEDICAMENTO: ' + str(medicamento) + '\n')
    nota_individual.write('QUANTIDADE: ' + str(quantidade) + '\n')
    nota_individual.write('VALOR: ' + str(valor_t) + '\n')
    nota_individual.write('VALOR TOTAL: ' + str(valor_total) + '\n')
    nota_individual.write('MÉTODO DE PAGAMENTO: ' + str(pagamento) + '\n')
    nota_individual.close()

    nota_vendas = open('vendas.txt', 'a', encoding='utf8')
    nota_vendas.write('\nDATA DA COMPRA: ' + str(data) + '\n')
    nota_vendas.write('VENDEDOR: ' + str(matricula) + '\n')
    nota_vendas.write('CPF DO CLIENTE: ' + str(cpf) + '\n')
    nota_vendas.write('NOME DO CLIENTE: ' + nome_completo + '\n')
    nota_vendas.write('MEDICAMENTO: ' + str(medicamento) + '\n')
    nota_vendas.write('QUANTIDADE: ' + str(quantidade) + '\n')
    nota_vendas.write('VALOR: ' + str(valor_t) + '\n')
    nota_vendas.write('VALOR TOTAL: ' + str(valor_total) + '\n')
    nota_vendas.write('MÉTODO DE PAGAMENTO: ' + str(pagamento) + '\n')
    nota_vendas.close()

vendas()
