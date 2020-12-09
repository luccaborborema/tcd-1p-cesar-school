import sys

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


opcao = 0


def menu():
    global opcao
    try:
        print('1 - CLIENTES')
        print('2 - FUNCIONÁRIOS')
        print('3 - MEDICAMENTOS')
        print('4 - ENCERRAR')
        opcao = int(input('DIGITE A SEÇÃO QUE DESEJA ACESSAR: '))
    except ValueError:
        print('\nVOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 4! TENTE NOVAMENTE: \n')
        menu()
    while opcao != -1:
        if opcao == 1:
            print('\nOPÇÃO ESCOLHIDA: CLIENTES\n')
            cliente()
        elif opcao == 2:
            print('\nOPÇÃO ESCOLHIDA: FUNCIONÁRIOS\n')
            funcionario()
        elif opcao == 3:
            print('\nOPÇÃO ESCOLHIDA: MEDICAMENTOS\n')
            medicamento()
        elif opcao == 4:
            sys.exit()
        else:
            print('\nVOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 4! TENTE NOVAMENTE: \n')
            menu()
def cliente():
    global opcao
    try:
        print('1 - CADASTRAR CLIENTE')
        print('2 - EDITAR CLIENTE')
        print('3 - REMOVER CLIENTE')
        print('4 - BUSCAR CLIENTE')
        print('5 - LISTAR CLIENTES')
        print('6 - VOLTAR')
        opcao = int(input('DIGITE UMA DAS OPÇÕES ACIMA: '))

    except ValueError:
        print('\nVOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 6! TENTE NOVAMENTE: \n')
        cliente()

    while opcao != -1:
        if opcao == 1:
            print('\nOPÇÃO ESCOLHIDA: CADASTRAR CLIENTE')
            cont = ""
            while cont != 'SAIR':
                try:
                    cpf = int(input('\nCPF (APENAS NÚMEROS): '))
                except ValueError:
                    print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO APENAS NÚMEROS!')
                    cpf = int(input('\nCPF (APENAS NÚMEROS): '))
                nome = input('NOME: ')
                try:
                    ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                    data = ddn.split('-')
                    ano = data[2]
                    ano_atual = 2020
                    idade = ano_atual - int(ano)
                except IndexError:
                    print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                    ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                    data = ddn.split('-')
                    ano = data[2]
                    ano_atual = 2020
                    idade = ano_atual - int(ano)
                clientes = open('clientes.txt', 'a', encoding='utf8')
                clientes.write('CPF: ' + str(cpf) + '\n')
                clientes.write('NOME: ' + nome + '\n')
                clientes.write('DATA DE NASCIMENTO: ' + ddn + '\n')
                clientes.write('IDADE: ' + str(idade) + '\n\n')
                clientes.close()
                print('\nCLIENTE CADASTRADO COM SUCESSO!\n')
                cont = str(input(
                    "PRESSIONE ENTER PARA CADASTRAR MAIS UM CLIENTE, OU 'SAIR', PARA VOLTAR AO MENU: "))
        elif opcao == 2:

            print('\nOPÇÃO ESCOLHIDA: EDITAR CLIENTE\n')
            try:
                nome = input('DIGITE O NOME DO CLIENTE: ')
                arq = ler_arquivo('clientes.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            except ValueError:
                print('VOCÊ DIGITOU UM NOME INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                nome = input('DIGITE O NOME DO CLIENTE: ')
                arq = ler_arquivo('clientes.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            print('O CADASTRO ATUAL DE', nome.upper(), ':')
            for a in range(0, 4):
                print(arq[i + a])
            print('DIGITE OS NOVOS DADOS DO CLIENTE: ')
            try:
                cpf = int(input('\nCPF (APENAS NÚMEROS): '))
            except ValueError:
                print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO APENAS NÚMEROS!')
                cpf = int(input('\nCPF (APENAS NÚMEROS): '))
            nome = input('NOME: ')
            try:
                ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                data = ddn.split('-')
                ano = data[2]
                ano_atual = 2020
                idade = ano_atual - int(ano)
            except IndexError:
                print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                data = ddn.split('-')
                ano = data[2]
                ano_atual = 2020
                idade = ano_atual - int(ano)
            arq[i] = 'CPF: ' + str(cpf) + '\n'
            arq[i + 1] = 'NOME: ' + nome + '\n'
            arq[i + 2] = 'DATA DE NASCIMENTO: ' + ddn + '\n'
            arq[i + 3] = 'IDADE: ' + str(idade) + '\n\n'
            arq2 = open("clientes.txt", 'w', encoding='utf8')
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            print('\nCLIENTE EDITADO COM SUCESSO!\n')
            cliente()

        elif opcao == 3:
            print('\nOPÇÃO ESCOLHIDA: REMOVER CLIENTE\n')
            try:
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('clientes.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            except ValueError:
                print('VOCÊ DIGITOU UM NOME INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('clientes.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            for a in range(0, 4):
                arq.pop(i)
            arq2 = open('clientes.txt', 'w', encoding='utf8')
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            print('\nCLIENTE REMOVIDO COM SUCESSO!\n')
            cliente()
        elif opcao == 4:
            print('\nOPÇÃO ESCOLHIDA: BUSCAR CLIENTE\n')
            print("1 - BUSCAR POR CPF \n2 - BUSCAR POR NOME\n")
            opcao = int(input("Digite a opção:"))
            if opcao == 1:
                try:
                    cpf = input('DIGITE O CPF: ')
                    arq = ler_arquivo('clientes.txt')
                    i = arq.index('CPF: ' + cpf + '\n')
                    for a in range(0, 4):
                        print(arq[i + a])
                except ValueError:
                    print('VOCÊ DIGITOU UM CPF INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                    cpf = input('DIGITE O CPF: ')
                    arq = ler_arquivo('clientes.txt')
                    i = arq.index('CPF: ' + cpf + '\n')
                    for a in range(0, 4):
                        print(arq[i + a])
            elif opcao == 2:
                try:
                    nome = input('DIGITE O NOME: ')
                    arq = ler_arquivo('clientes.txt')
                    i = arq.index('NOME: ' + nome + '\n')
                    for a in range(0, 4):
                        print(arq[i + a])
                except ValueError:
                    print('VOCÊ DIGITOU UM NOME INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                    nome = input('DIGITE O NOME: ')
                    arq = ler_arquivo('clientes.txt')
                    i = arq.index('NOME: ' + nome + '\n')
                    for a in range(0, 4):
                        print(arq[i + a])
            cliente()

        elif opcao == 5:
            print('\nOPÇÃO ESCOLHIDA: LISTAR CLIENTES\n')
            listar('clientes.txt')
            cliente()

        elif opcao == 6:
            print('\nOPÇÃO ESCOLHIDA: VOLTAR\n')
            menu()


def funcionario():
    global opcao
    print('1 - CADASTRAR FUNCIONÁRIO')
    print('2 - EDITAR FUNCIONÁRIO')
    print('3 - REMOVER FUNCIONÁRIO')
    print('4 - BUSCAR FUNCIONÁRIO')
    print('5 - LISTAR FUNCIONÁRIO')
    print('6 - VOLTAR')
    try:
        opcao = int(input('DIGITE UMA DAS OPÇÕES ACIMA: '))
    except ValueError:
        print('\nVOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 6! TENTE NOVAMENTE: \n')
        funcionario()
    while opcao != -1:
        if opcao == 1:
            print('\nOPÇÃO ESCOLHIDA: CADASTRAR FUNCIONÁRIO')
            cont = ""
            while cont != 'sair':
                try:
                    matricula = int(input('\nMATRÍCULA: '))
                except ValueError:
                    print('MATRÍCULA INVÁLIDA! CERTIFIQUE-SE QUE ESTÁ DIGITANDO APENAS NÚMEROS E TENTE NOVAMENTE!')
                    matricula = int(input('\nMATRÍCULA: '))
                nome = input('NOME: ')
                try:
                    ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                    data = ddn.split('-')
                    ano = data[2]
                    ano_atual = 2020
                    idade = ano_atual - int(ano)
                except IndexError:
                    print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                    ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                    data = ddn.split('-')
                    ano = data[2]
                    ano_atual = 2020
                    idade = ano_atual - int(ano)
                try:
                    dda = input('DATA DE ADMISSÃO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                except IndexError:
                    print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                    dda = input('DATA DE ADMISSÃO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                funcionarios = open('funcionarios.txt', 'a', encoding='utf8')
                funcionarios.write('MATRÍCULA: ' + str(matricula) + '\n')
                funcionarios.write('NOME: ' + nome + '\n')
                funcionarios.write('DATA DE NASCIMENTO: ' + ddn + '\n')
                funcionarios.write('IDADE: ' + str(idade) + '\n')
                funcionarios.write('DATA DE ADMISSÃO: ' + str(dda) + '\n\n')
                funcionarios.close()
                print('\nFUNCIONÁRIO CADASTRADO COM SUCESSO!\n')
                cont = input(
                    "PRESSIONE ENTER PARA CADASTRAR MAIS UM FUNCIONÁRIO, OU 'SAIR', PARA VOLTAR AO MENU: ")
                if cont == 'SAIR':
                    funcionario()
        elif opcao == 2:
            print('\nOPÇÃO ESCOLHIDA: EDITAR FUNCIONÁRIO\n')
            try:
                nome = input('DIGITE O NOME DO FUNCIONÁRIO: ')
                arq = ler_arquivo('funcionarios.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            except ValueError:
                print('VOCÊ DIGITOU UM NOME INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                nome = input('DIGITE O NOME DO FUNCIONÁRIO: ')
                arq = ler_arquivo('funcionarios.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            print('O CADASTRO ATUAL DE', nome.upper(), ':')
            for a in range(0, 4):
                print(arq[i + a])
            print('DIGITE OS NOVOS DADOS DO FUNCIONÁRIO: ')
            try:
                matricula = int(input('\nMATRÍCULA: '))
            except ValueError:
                print('MATRÍCULA INVÁLIDA! CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO APENAS NÚMEROS E TENTE NOVAMENTE!')
                matricula = int(input('\nMATRÍCULA: '))
            nome = input('NOME: ')
            try:
                ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                data = ddn.split('-')
                ano = data[2]
                ano_atual = 2020
                idade = ano_atual - int(ano)
            except IndexError:
                print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                ddn = input('DATA DE NASCIMENTO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
                data = ddn.split('-')
                ano = data[2]
                ano_atual = 2020
                idade = ano_atual - int(ano)
            try:
                dda = input('DATA DE ADMISSÃO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
            except IndexError:
                print('CERTIFIQUE-SE DE QUE ESTÁ DIGITANDO A DATA NO FORMATO DD-MM-YYY (EX: 11-22-3333):')
                dda = input('DATA DE ADMISSÃO NO FORMATO DD-MM-YYY (EX: 11-22-3333): ')
            arq[i] = 'MATRÍCULA: ' + str(matricula) + '\n'
            arq[i + 1] = 'NOME: ' + nome + '\n'
            arq[i + 2] = 'DATA DE NASCIMENTO: ' + ddn + '\n'
            arq[i + 3] = 'IDADE: ' + str(idade) + '\n'
            arq[i + 4] = 'DATA DE ADMISSÃO: ' + str(dda) + '\n\n'
            arq2 = open("funcionarios.txt", 'w', encoding='utf8')
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            print('\nFUNCIONÁRIO EDITADO COM SUCESSO!\n')
            funcionario()

        elif opcao == 3:
            print('\nOPÇÃO ESCOLHIDA: REMOVER FUNCIONÁRIO\n')
            try:
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('funcionarios.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            except ValueError:
                print('VOCÊ DIGITOU UM NOME INVÁLIDO OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('funcionarios.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            for a in range(0, 5):
                arq.pop(i)
            arq2 = open('funcionarios.txt', 'w', encoding='utf8')
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            print('\nFUNCIONÁRIO REMOVIDO COM SUCESSO!\n')
            funcionario()
        elif opcao == 4:
            print('\nOPÇÃO ESCOLHIDA: BUSCAR FUNCIONÁRIO\n')
            print("1 - BUSCAR POR MATRICULA \n2 - BUSCAR POR NOME\n")
            opcao = int(input("DIGITE UMA DAS OPÇÕES ACIMA:"))
            if opcao == 1:
                try:
                    matricula = input('DIGITE A MATRÍCULA: ')
                    arq = ler_arquivo('funcionarios.txt')
                    i = arq.index('MATRÍCULA: ' + matricula + '\n')
                    for a in range(0, 5):
                        print(arq[i + a])
                except ValueError:
                    print('VOCÊ DIGITOU UMA MATRÍCULA INVÁLIDA OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                    matricula = input('DIGITE A MATRÍCULA: ')
                    arq = ler_arquivo('funcionarios.txt')
                    i = arq.index('MATRÍCULA: ' + matricula + '\n')
                    for a in range(0, 5):
                        print(arq[i + a])
            elif opcao == 2:
                try:
                    nome = input('DIGITE O NOME: ')
                    arq = ler_arquivo('funcionarios.txt')
                    i = arq.index('NOME: ' + nome + '\n')
                    for a in range(0, 5):
                        print(arq[i + a])
                except ValueError:
                    print('VOCÊ DIGITOU UMA MATRÍCULA INVÁLIDA OU QUE NÃO ESTÁ CADASTRADO NO SISTEMA! TENTE NOVAMENTE: ')
                    nome = input('DIGITE O NOME: ')
                    arq = ler_arquivo('funcionarios.txt')
                    i = arq.index('NOME: ' + nome + '\n')
                    for a in range(0, 5):
                        print(arq[i + a])
            funcionario()

        elif opcao == 5:
            print('\nOPÇÃO ESCOLHIDA: LISTAR FUNCIONÁRIOS\n')
            listar('funcionarios.txt')
            funcionario()

        elif opcao == 6:
            print('\nOPÇÃO ESCOLHIDA: VOLTAR\n')
            menu()


def medicamento():
    global opcao
    print('1 - CADASTRAR MEDICAMENTO')
    print('2 - EDITAR MEDICAMENTO')
    print('3 - REMOVER MEDICAMENTO')
    print('4 - BUSCAR MEDICAMENTO')
    print('5 - LISTAR MEDICAMENTO')
    print('6 - VOLTAR')
    try:
        opcao = int(input('DIGITE UMA DAS OPÇÕES ACIMA: '))
    except ValueError:
        print('\nVOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 6! TENTE NOVAMENTE: \n')
        opcao = int(input('DIGITE UMA DAS OPÇÕES ACIMA: '))
    while opcao != -1:
        if opcao == 1:
            print('\nOPÇÃO ESCOLHIDA: CADASTRAR MEDICAMENTO')
            cont = ""
            while cont != 'sair':
                try:
                    nome = input('\nNOME: ')
                except NameError:
                    print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O NOME CERTO!")
                    nome = input('\nNOME: ')
                try:
                    lab = input('LABORATÓRIO: ')
                except NameError:
                    print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O LABORATORIO CERTO!")
                    lab = input('LABORATÓRIO: ')
                try:
                    valor = float(input('VALOR: '))
                except ValueError:
                    print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O VAL0R CERTO!")
                    valor = float(input('VALOR: '))
                try:
                    tipo = int(input('1 - SIM\n2 - NÃO\nGENÉRICO: '))
                except ValueError:
                    print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O TIPO CERTO!")
                    tipo = int(input('1 - SIM\n2 - NÃO\nGENÉRICO: '))
                if tipo == 1:
                    tipo = False

                elif tipo == 2:
                    tipo = True
                try:
                    quant = int(input('QUANTIDADE: '))
                except ValueError:
                    print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO A QUANTIDADE CERTA")
                    quant = int(input('QUANTIDADE: '))
                medicamentos = open('medicamentos.txt', 'a', encoding='utf8')
                medicamentos.write('NOME: ' + nome + '\n')
                medicamentos.write('LABORATÓRIO: ' + lab + '\n')
                medicamentos.write('VALOR: ' + str(valor) + '\n')
                medicamentos.write('GENÉRICO: ' + str(tipo) + '\n')
                medicamentos.write('QUANTIDADE: ' + str(quant) + '\n\n')
                medicamentos.close()
                print('\nMEDICAMENTO CADASTRADO COM SUCESSO!\n')
                cont = input("PRESSIONE ENTER PARA CADASTRAR MAIS UM MEDICAMENTO, OU 'SAIR', PARA VOLTAR AO MENU: ")
                if cont == 'SAIR':
                    medicamento()
        elif opcao == 2:
            print('\nOPÇÃO ESCOLHIDA: EDITAR MEDICAMENTO\n')
            try:
                nome = input('DIGITE O NOME DO MEDICAMENTO: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O NOME CERTO!")
                nome = input('DIGITE O NOME DO MEDICAMENTO: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
            print('O CADASTRO ATUAL DE', nome.upper(), ':')
            for a in range(0, 5):
                print(arq[i + a])
            print('DIGITE OS NOVOS DADOS DO MEDICAMENTO: ')
            try:
                nome = input('\nNOME: ')
            except NameError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O NOME CERTO!")
                nome = input('\nNOME: ')
            try:
                lab = input('LABORATÓRIO: ')
            except NameError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O LABORATORIO CERTO!")
                lab = input('LABORATÓRIO: ')
            try:
                valor = float(input('VALOR: '))
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O VAL0R CERTO!")
                valor = float(input('VALOR: '))
            try:
                tipo = int(input('1 - SIM\n2 - NÃO\nGENÉRICO: '))
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O TIPO CERTO!")
                tipo = int(input('1 - SIM\n2 - NÃO\nGENÉRICO: '))
            if tipo == 1:
                tipo = True

            elif tipo == 2:
                tipo = False
            try:
                quant = int(input('QUANTIDADE: '))
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO A QUANTIDADE CERTA")
                quant = int(input('QUANTIDADE: '))
            arq[i] = 'NOME: ' + nome + '\n'
            arq[i + 1] = 'LABORATÓRIO: ' + lab + '\n'
            arq[i + 2] = 'VALOR: ' + str(valor) + '\n'
            arq[i + 3] = 'GENÉRICO: ' + str(tipo) + '\n'
            arq[i + 4] = 'QUANTIDADE: ' + str(quant) + '\n\n'
            arq2 = open("medicamentos.txt", 'w', encoding='utf8')
            for i in range(0, len(arq)):
                arq2.write(arq[i])
            arq2.close()
            print('\nMEDICAMENTO EDITADO COM SUCESSO!\n')
            medicamento()

        elif opcao == 3:
            print('\nOPÇÃO ESCOLHIDA: REMOVER MEDICAMENTO\n')
            try:
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
                for a in range(0, 5):
                    arq.pop(i)
                arq2 = open('medicamentos.txt', 'w', encoding='utf8')
                for i in range(0, len(arq)):
                    arq2.write(arq[i])
                arq2.close()
                print('\nMEDICAMENTO REMOVIDO COM SUCESSO!\n')
                medicamento()
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O NOME CERTO!")
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                i -= 1
                for a in range(0, 5):
                    arq.pop(i)
                arq2 = open('medicamentos.txt', 'w', encoding='utf8')
                for i in range(0, len(arq)):
                    arq2.write(arq[i])
                arq2.close()
                print('\nMEDICAMENTO REMOVIDO COM SUCESSO!\n')
                medicamento()
        elif opcao == 4:
            print('\nOPÇÃO ESCOLHIDA: BUSCAR MEDICAMENTO\n')
            try:
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                for a in range(0, 5):
                    print(arq[i + a])
                medicamento()
            except ValueError:
                print("CERTIFIQUE-SE DE QUE ESTA DIGITANDO O NOME CERTO!")
                nome = input('DIGITE O NOME: ')
                arq = ler_arquivo('medicamentos.txt')
                i = arq.index('NOME: ' + nome + '\n')
                for a in range(0, 5):
                    print(arq[i + a])
                medicamento()
        elif opcao == 5:
            print('\nOPÇÃO ESCOLHIDA: LISTAR MEDICAMENTOS\n')
            listar('medicamentos.txt')
            medicamento()

        elif opcao == 6:
            print('\nOPÇÃO ESCOLHIDA: VOLTAR\n')
            menu()


menu()