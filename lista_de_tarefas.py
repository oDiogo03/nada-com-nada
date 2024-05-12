opcao_do_menu = 0

def menu():
    print(25*"*")
    print('1 - Incluir nova tarefa')
    print('2 - Ver lista de tarefas')
    print('3 - Excluir tarefa salva')
    print('4 - Sair')
    print(25*"*")

menu()
lista_de_tarefas = []
opcao_do_menu = int(input('\nDigite o número da opção desejada: '))

while True:
    if opcao_do_menu == 1:
        print('Opção escolhida : 1 - Incluir tarefa')
        opcao_do_menu = 0
        tarefa = input('Digite tarefa a ser adicionada: ')
        lista_de_tarefas.append(tarefa)
        print('\nSua lista de tarefas')
        print(lista_de_tarefas)
        print('\n')
        menu()
        opcao_do_menu = int(input('\nDigite o número da opção desejada: '))

    elif opcao_do_menu == 2:
        print('Opção escolhida: 2 - Ver lista de tarefas')
        print('\nSua lista de tarefas: ')
        print('\n')
        opcao_do_menu = 0
        menu()
        opcao_do_menu = int(input('\nDigite o número da opção desejada: '))

    elif opcao_do_menu == 3:
        print('Opção escolhida: 3 - Excluir tarefa salva')
        print('\nSua lista de tarefas: ')
        print(lista_de_tarefas)
        print('\n')
        tarefa_a_ser_removida = input('Digite a tarefa a ser removida: ')
        lista_de_tarefas.remove(tarefa_a_ser_removida)
        print('\nSua lista de tarefas: ')
        print(lista_de_tarefas)
        print('\n')
        opcao_do_menu = 0
        menu()
        opcao_do_menu = int(input('\nDigite o número da opção desejada: '))

    elif opcao_do_menu == 4:
        print('Opção escolhida: 4 - Excluir tarefa salva')
        resposta_de_saida = input('Deseja mesmo sair? (S/N) ').upper()
        if (resposta_de_saida == 'S') or (resposta_de_saida == 'SIM'):
            break
        else:
            print('\n')
            menu()
            opcao_do_menu = 0 
            opcao_do_menu = int(input('\nDigite o número da opção desejada: '))