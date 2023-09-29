# Programa de Sistema de Cadastro


# Modulos importados
# Para gerar o numero aleatório da matrícula
import random
# Para pedir pro sistema operacional deletar o arquivo
import os


# Classe

class DadosDeMatricula:
    def __init__(self, user_matricula, user_nome, user_cpf, user_nascimento, user_peso, user_email, user_agendamento):
        self.user_matricula = user_matricula
        self.user_nome = user_nome
        self.user_cpf = user_cpf
        self.user_nascimento = user_nascimento
        self.user_peso = user_peso
        self.user_email = user_email
        self.user_agendamento = user_agendamento

    # funões para chamar a classe por dentro da classe.
    def printar_consulta_matricula(self):
        print("Os dados da matrícula consultada são:\n")
        print(self.user_matricula, self.user_nome, self.user_cpf, self.user_nascimento, self.user_peso, self.user_email,
              self.user_agendamento)

    def printar_alteracao_dados_matricula(self):
        print("Os dados da foram alterados com sucesso:\n")
        print(self.user_matricula, self.user_nome, self.user_cpf, self.user_nascimento, self.user_peso, self.user_email,
              self.user_agendamento)


# Funções

# A função registra informações do usuario
# cria o arquivo txt
# Atribui ao nome do arquivo a matricula gerada aleatoriamente da função gerar_matricula
# utiliza a variavel atribuida a classe

def criar_cadastro_user(nome_arquivo):
    user_nome = input('Digite seu nome:\n')
    user_cpf = input('Digite o numero do CPF sem pontos ou traços:\n')
    user_nascimento = input('Digite a data de nascimento com barras:\n')
    user_peso = float(input('Digite o peso:\n'))
    user_email = input('Digite o e-mail:\n')
    user_agendamento = input('Digite o numero de agendamento:\n')

    # para evitar erros, e tb informar ao usuario se o arquivo foi criado com sucesso.
    try:
        with open(nome_arquivo + ".txt", "w") as arquivo:
            arquivo.write(f"{nome_arquivo}\n")
            arquivo.write(f"{user_nome}\n")
            arquivo.write(f"{user_cpf}\n")
            arquivo.write(f"{user_nascimento}\n")
            arquivo.write(f"{user_peso}\n")
            arquivo.write(f"{user_email}\n")
            arquivo.write(f"{user_agendamento}\n")

        print(f"Parabéns o arquivo {nome_arquivo} foi criado com sucesso! \n")

    except IOError:
        print(f"Não foi possível criar o arquivo {nome_arquivo}. =/ ")


# Função consultar

def consulta_matricula():
    try:

        input_matricula = input("Digite o nome do arquivo a ser consultado: ")
        consulta = open(f'{input_matricula}.txt', "r")
        linhas = consulta.readlines()
        return (linhas)

    except IOError:

        print(f"Não foi possível criar o arquivo {input_matricula}. =/")


# Função alteração
# Abre arquivo alvo do input
# pergunta item da lista a alterar
# abre o arquivo no modo escrita para escrever

def menu_alterar_dados():
    try:
        input_matricula = input("Digite o nome da matrícula a ser alterada: ")
        consulta = open(f'{input_matricula}.txt', "r")
        linhas = consulta.readlines()

        print("0 - Matrícula\n1 - Nome\n2 - CPF\n3 - Data Nascimento\n4 - Peso\n5 - E-mail\n6 - Agendamento\n")
        input_escolha_alterar = int(input('Digite o número correspondente à opção desejada: \n'))

        if input_escolha_alterar >= 0 and input_escolha_alterar < len(linhas):  # terminar elifs e elses
            input_alterar = input("Digite o novo texto:")
            # N funciona sem o "/n", acaba apagando itens do txt e para consultar depois da erro.
            linhas[input_escolha_alterar] = input_alterar + "\n"

        escrever = open(f'{input_matricula}.txt', "w")
        # Escreve todas as linhas de volta para o arquivo
        escrever.writelines(linhas)

        user_dados1 = DadosDeMatricula(linhas[0], linhas[1], linhas[2], linhas[3], linhas[4], linhas[5], linhas[6])
        user_dados1.printar_alteracao_dados_matricula()

    except FileNotFoundError:
        print(f"O arquivo {input_matricula}, não foi encontrado!")

    except ValueError:
        print(f"A opção digitada {input_escolha_alterar}, é invalida!")

    except IOError:
        print(f"Erro ao alterar o arquivo {input_matricula}!")


# Função Exclusão

def excluir_matricula():
    try:
        user_excluir = input("Digite a matricula do arquivo que deseja deletar: ")
        if os.path.exists(user_excluir + ".txt"):
            user_confirmar_excluir = input(f"Confirme a exclusão do, '{user_excluir}.txt', \n 1- Sim \n 2- Não \n")
            if user_confirmar_excluir == "1":
                os.remove(user_excluir + ".txt")
                print(f"o Arquivo, '{user_excluir}.txt', foi excluído com sucesso!")


    except FileExistsError:
        print(f"o Arquivo, '{user_excluir}.txt', não existe!")


# Função de Menu (Menu)
def menu():
    # Contador adicionado para gerar novo arquivo
    contador = 1

    # while true é melhor com input e para loop infinito, ate determinada instrução # OBS: estrutura de repetição, ela foi criada dentro do menu para repetir esse bloco, que repetira tudo. ao final dava problema na criação de arquivos novos.
    while True:

        # A estrutura try-except é usada para lidar com exceções no Python, ajuda a evitar erros.
        try:
            print(
                "1 - Cadastro de matrícula \n2 - Consulta de matrícula cadastrada\n3 - Alterar matrícula cadastrada\n4 - Exclusão de matrícula\n5 - Sair/Encerrar")
            escolha = int(input('Digite o número correspondente a opção desejada: \n'))

            if escolha == 1:

                # tive que deixar o numero da matricula como string para atribuir ao .txt
                sequencia_numeros = random.sample(range(0, 10), 5)
                sequencia_numeros_gerada = int(''.join(map(str, sequencia_numeros)))
                nome_arquivo = f"2023{sequencia_numeros_gerada + contador}"

                # chamando a funçao de criar_arquivo_matricula_gerada
                # utilizando a sequencia numerica criada pela função gerar_matricula
                criar_cadastro_user(nome_arquivo)
                contador += 1

            elif escolha == 2:

                try:
                    linhas = consulta_matricula()
                    user_dados1 = DadosDeMatricula(linhas[0], linhas[1], linhas[2], linhas[3], linhas[4], linhas[5],
                                                   linhas[6])
                    user_dados1.printar_consulta_matricula()

                except FileNotFoundError:
                    print(f"O arquivo não foi encontrado.")
                except IOError:
                    print("Erro ao ler o arquivo.")

            elif escolha == 3:

                try:
                    menu_alterar_dados()

                except FileNotFoundError:
                    print(f"O arquivo não foi encontrado.")

                except IOError:
                    print("Erro ao alterar o arquivo.")

            elif escolha == 4:
                try:
                    excluir_matricula()

                except IOError:
                    print("Erro ao excluir o arquivo.")

            elif escolha == 5:

                print("Deseja realmente sair?\n1 - Sim\n2 - Não\n")
                escolha2 = int(input("Digite a sua opção:\n"))

                # confirmação de encerramento, aninhamento de condicionais.
                if escolha2 == 1:
                    break

                elif escolha2 == 2:
                    continue

                else:
                    print("Favor escolher uma opção válida")

        # ValueError é uma exceção levantada quando um valor não é válido para uma operação ou função específica.
        except ValueError:
            print("Isso não é uma opção válida, tente novamente:\n")


# chamar a função menu para rodar o while e o programa
menu()