import os
import time

# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa')
# Lista para armazenar os dados das pessoas
dados = []

# Função para inserir uma nova pessoa
def inserir():
    # Coleta os dados da nova pessoa
    pessoa = {
        chaves[0]: input('Informe o nome da pessoa que deseja adicionar: '),
        chaves[1]: input('Informe o CPF da pessoa que deseja adicionar: '),
        chaves[2]: input('Informe o Telefone da pessoa que deseja adicionar: '),
        chaves[3]: input('Informe o E-mail da pessoa que deseja adicionar: '),
        chaves[4]: input('Informe a Profissão da pessoa que deseja adicionar: '),
        chaves[5]: input('Informe o nome da Empresa que a pessoa trabalha: ')
    }
    print('Inserindo Dados...')
    time.sleep(2)  # Espera por 2 segundos para simular a inserção
    dados.append(pessoa)  # Adiciona a nova pessoa à lista 'dados'
    print('Cadastro realizado com sucesso!')
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
    
    # Pergunta ao usuário se deseja voltar ao menu principal ou sair do programa
    while True:
        opcao = input("Deseja voltar ao menu principal (s) ou sair do programa (n)? ").lower()
        if opcao == 's':
            break
        elif opcao == 'n':
            print("Saindo do programa...")
            time.sleep(2) # Espera por 2 segundos para simular saida do programa.
            exit()
        else:
            print("Opção inválida. Por favor, escolha 's' para voltar ao menu principal ou 'n' para sair do programa.")


# Função para listar os dados e informações
def listar_dados():
    if not dados:
        print("Nenhum dado cadastrado...")  # Informa se não há dados cadastrados
    else:
        print('Pesquisando Dados...')# Mensagem de espera e tempo de espera
        time.sleep(2)  # Espera por 2 segundos para simular a pesquisa.
        for i, pessoa in enumerate(dados):
            print(f"{i+1}.")  # Exibe o número da pessoa na lista
            for chave, valor in pessoa.items():
                print(f"{chave}: {valor}")  # Exibe cada par chave-valor da pessoa
            print(f'-'*20)  # Linha separadora entre as pessoas
 
    # Mensagem de sucesso
    print('Dados listados com sucesso!')

# Função para pesquisar dados pelo nome
def pesquisar_dados(nome):
    resultados = [pessoa for pessoa in dados if nome.lower() in pessoa['Nome'].lower()]  # Filtra as pessoas pelo nome
    if resultados:
        print("Registros encontrados:")
        time.sleep(2) # Espera por 2 segundos para simular a pesquisa.
        for pessoa in resultados:
            for chave, valor in pessoa.items():
                print(f"{chave}: {valor}")  # Exibe cada par chave-valor das pessoas encontradas
            print(f'-'*20)  # Linha separadora entre as pessoas
    else:
        print(f"Nenhum dado encontrado com o nome '{nome}'.")
    
def atualizar_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    pessoa = dados[indice - 1]  # Acessa a pessoa pelo índice
    for chave in chaves:
        novo_valor = input(f"{chave} atual ({pessoa[chave]}): ")  # Pergunta o novo valor de cada chave
        if novo_valor:
            pessoa[chave] = novo_valor  # Atualiza o valor se o usuário forneceu uma nova entrada
    


# Função para excluir um dado com base no índice fornecido
def excluir_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    dados.pop(indice - 1)  # Remove a pessoa pelo índice
    print(f"Item de índice {indice} removido com sucesso.")
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
    os.system('cls')  # Limpa a tela 

# Menu principal
def menu():
    while True:
        print(f"{'='*20} ESCOLHA UMA DAS OPÇÕES PARA INICIAR: {'='*20}")
        print("1. Inserir nova pessoa")
        print("2. Listar todos os dados")
        print("3. Pesquisar dados pelo nome")
        print("4. Atualizar dados de uma pessoa")
        print("5. Excluir dados de uma pessoa")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        os.system('cls')  # Limpa a tela 

        if opcao == '1':
            inserir()
        elif opcao == '2':
            listar_dados()
        elif opcao == '3':
            nome = input("Informe o nome que deseja pesquisar: ")
            pesquisar_dados(nome)
        elif opcao == '4':
            listar_dados()
            indice = int(input("Informe o índice da pessoa que deseja atualizar: "))
            atualizar_dados(indice)
            # Pergunta ao usuário se deseja voltar ao menu principal ou sair do programa
           
        elif opcao == '5':
            listar_dados()
            indice = int(input("Informe o índice da pessoa que deseja excluir: "))
            excluir_dados(indice)
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
