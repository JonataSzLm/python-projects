AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('')
        print('>>>>>  A agenda está vazia!  <<<<<\n')

def buscar_contato(contato):
    try:
        print('')
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-mail:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('___________________________________________')
    except KeyError:
        print('')
        print('>>>>>  Contato {} inexistente!  <<<<<\n'.format(contato))
    except Exception as e:
        print('')
        print('>>>>>  Um erro inesperado ocorreu :(  <<<<<\n')
        print(e)


def ler_detalhes_contato():
    telefone = input('Insira o telefone: ')
    email = input('Insira o email: ')
    endereco = input('Insira o endereco: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('')
    print('>>>>>  Contato {} adicionado/editado com sucesso!  <<<<<\n'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('')
        print('>>>>>  Contato {} excluido com sucesso!  <<<<<\n'.format(contato))
    except KeyError:
        print('')
        print('>>>>>  Contato {} inexistente!  <<<<<\n'.format(contato))
    except Exception as e:
        print('')
        print('>>>>>  Um erro inesperado ocorreu :(  <<<<<\n')
        print(e)


def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{};{};{};{}\n'.format(contato, telefone, email, endereco))
        print('')
        print('>>>>>  Agenda exportada com sucesso!  <<<<<<\n')
    except Exception as e:
        print('')
        print('>>>>>  Algum erro ocorreu ao exportar contatos!  <<<<<\n')
        print(e)


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
        print('')
        print('>>>>>  Importação realizada com sucesso!  <<<<<\n')

    except FileNotFoundError:
        print('>>>>>  Arquivo não encontrado!  <<<<<\n')
    except Exception as e:
        print('>>>>>  Um erro inesperado ocorreu :(  <<<<<\n')


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }

            print('>>>>>  Base de dados carregada com sucesso!  <<<<<')
            print('>>>>>  {} contatos carregados  <<<<<\n'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>>>  A base de dados não foi encontrada!  <<<<<\n')
    except Exception as e:
        print('>>>>>  Um erro inesperado ocorreu :(  <<<<<\n')


def imprimir_menu():
    print('')
    print('1: Mostrar todos os contatos da agenda')
    print('2: Buscar contato')
    print('3: Incluir contato')
    print('4: Editar contato')
    print('5: Excluir contato')
    print('6: Exportar contatos para CSV')
    print('7: Importar contatos de um arquivo CSV')
    print('0: Fechar agenda')
    print('_____________________________________________\n')

# INICIO DO PROGRAMA

carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('')
        mostrar_contatos()
    elif opcao == '2':
        print('')
        contato = input('Insira o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        print('')
        contato = input('Insira o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>>  Contato {} já existe  <<<<<\n'.format(contato))
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        print('')
        contato = input('Insira o nome do contato: ')
        try:
            AGENDA[contato]
            print('')
            print('>>>>>  Editando contato: {}  <<<<<\n'.format(contato))
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('')
            print('>>>>>  Contato {} inexistente <<<<<\n'.format(contato))
    elif opcao == '5':
        contato = input('Insira o nome do contato a ser excluido: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_arquivo = input('Insira o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_arquivo)
    elif opcao == '7':
        nome_arquivo = input('Insira o nome do arquivo a ser importado: ')
        importar_contatos(nome_arquivo)
    elif opcao == '0':
        print('')
        print('>>>>>  Programa finalizado!  <<<<<\n')
        break

    else:
        print('')
        print('>>>>>  Opção invalida!!  <<<<<\n')
