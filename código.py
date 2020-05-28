# Como não sabemos como funciona o touch decidimos botar uma escolhas escritas para testar o código
import uuid

codigo_aleatorio = ""
mensagem_prof = ""
chamadas = 0
mensagem_alu = ""
opcao_0 = ""
notificacao_prof = 0
notificacao_alu = 0
codigo_0 = 0
presenca = 0
b = 0
a = 0
presentes = 0
horario = ""
print("LOGIN")
email = input("Digite seu e-mail: \n")  # E-mail que a cesar disponibilizará para os alunos
senha = input("Digite a sua senha: \n")  # A senha é o CPF do aluno
# O código vai conferir se o confere o e-mail com o cpf do aluno
nome = input("escreva seu nome:")  # decidimos botar essa parte para demonstrar a home
profissao = input("Qual a sua profissão:")
# Se for professor:
if profissao == "Professor":
    while b == 0:
        print("\n\nOLÁ,", nome, "\n\n")
        print("CHAMADA \nNova chamada \nEm andamento")
        print("HISTÓRICO")  # chamadas ja feitas retiradas do banco de dados da CESAR school
        print("TURMAS")  # Turmas do professor retiradas do banco de dados do CESAR school
        print("MENSAGENS-", notificacao_alu)
        print("PERFIL")
        opcao = input("")
        a = 0
        if opcao == "CHAMADA":
            print("Nova chamada \nEm andamento")
            opcao_0 = input("")
            if opcao_0 == "Nova chamada":
                while a == 0:
                    print(
                        "Turma 1 ")  # Turmas do professor retiradas do banco de dados do CESAR school que serão armazenadas dentro de uma lista

                    # O professor escolheu a turma 1
                    horario = input("Qual o horário a chamada será automaticamente encerrada:")


                    def my_random_string(string_length=10):
                        """Returns a random string of length string_length."""
                        random = str(uuid.uuid4())
                        random = random.upper()
                        random = random.replace("-", "")
                        return random[0:string_length]
                    codigo_aleatorio = my_random_string(6)


                    print("Seu código é:", codigo_aleatorio)
                    # Como não sabiamos como colocar geolocalização, decidimos fazer apenas o código por enquanto
                    chamadas = chamadas + 1
                    a = a + 1
            elif opcao_0 == "Em andamento":
                while a == 0:
                    if chamadas >= 1:
                        # Turmas do professor retiradas do banco de dados do CESAR school com chamadas salvas, e o professo escolheu a turma 1
                        print(codigo_aleatorio, "             ")
                        # Aqui mostraria os alunos da turma que marcaram presença
                        print("Tem certeza que deseja finalizar a chamada?(", presentes,
                              "alunos marcaram presença )\n A chamada será finalizada automaticamente as", horario, "horas.")
                        abcd = input('Digite sim ou não: ')

                        if abcd == "sim":
                            chamadas = chamadas - 1
                            print('Codigo encerrado')
                            codigo_aleatorio = ""
                        elif abcd == "não":
                            break


                    # Se sim, o código finaliza a chamada
                    # Se não, ele finaliza a chamada automaticamente no horário escolhido
                    a = a + 1
        elif opcao == "HISTÓRICO":
            while a == 0:
                print("")
                # chamadas ja feitas retiradas do banco de dados da CESAR school
                a = a + 1
        elif opcao == "TURMAS":
            print("")
            while a == 0:
                # Turmas do professor retiradas do banco de dados do CESAR school
                a = a + 1
        elif opcao == "MENSAGENS":
            while a == 0:
                print(mensagem_prof)
                # Mensagens recebidas não tem como serem feitas no momento, pois não sabemos salvar o código

                # O professor entra no banco de dados do cesar e escolhe a turma e o aluno que ele quer mandar mensagem
                mensagem_alu = input("")
                notificacao_prof += 1  # Mensagem vai ser será salva e mandada para o aluno e a notificação vai ficar em cima de mensagens
                a = a + 1
        elif opcao == "PERFIL":
            while a == 0:
                print(nome)
                print(email)
                print("\nHorários:")  # Os horários do dia vão ser pegos do banco de dados
                a = a + 1

    # Se for aluno:
if profissao == "Estudante":
    while b == 0:
        print("\n\nOLÁ,", nome, "\n\n")
        print("CHAMADA")  # colocar o código e confirmar presença
        print("TURMA")  # ACESSO AO HORÁRIO DE AULA DO BANCO DE DADOS
        print("MENSAGENS-", notificacao_prof)  # mensagens enviadas e recebidas
        print("PERFIL")
        opcao_1 = input("")
        a = 0
        if opcao_1 == "CHAMADA":
            while a == 0:
                codigo_0 = input("Escreva o código:")
                if codigo_0 == codigo_aleatorio:
                    print("Presença confirmada")
                    #como não sabemos utilizar geolocalização, decidimos botar só o código no momento
                    presentes += 1
                else:
                    print("Você não está na sala de aula")
                a = a + 1
        elif opcao_1 == "TURMA":
            while a == 0:
                print("")
                # horário em TABELA do dia
                a = a + 1
        elif opcao_1 == "MENSAGENS":
            while a == 0:
                print(mensagem_alu)
                # Mensagens recebidas não tem como serem feitas no momento, pois não sabemos salvar o código

                # O aluno entra no banco de dados do cesar e escolhe a turma e o professor que ele quer mandar mensagem
                mensagem_prof = input("")
                notificacao_alu += 1
                # Mensagem vai ser será salva e mandada para o professor e a notificação vai ficar em cima de mensagens
                a = a + 1
        elif opcao_1 == "PERFIL":
            while a == 0:
                # nome social,email,foto do perfil, e horário
                print(nome)
                print(email)
                print("\nHorários:")  # Os horários do dia vão ser pegos do banco de dados
                a = a + 1
